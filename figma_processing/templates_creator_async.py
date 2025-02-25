import aiohttp
import asyncio
from loguru import logger
from pathlib import Path
from typing import Dict, Any
from config.settings import TEMPLATES_PATH
from constants.fields import pages
import os
from urllib.parse import urljoin

# Проверка существования шаблонов


def is_templates_exist(names: tuple) -> bool:
    result = True
    for name in names:
        name = f'{name}.png'
        file_template = TEMPLATES_PATH / name
        result *= file_template.exists()
        if result:
            logger.info(f'Шаблон {name} существует')
        else:
            return False
    return result

# Асинхронная функция для экспорта фреймов из Figma в PNG


async def export_figma_frames_to_png_async(token: str, file_key: str, pages: tuple, output_dir: str) -> bool:
    """
    Экспортирует указанные фреймы из Figma в формат PNG асинхронно.

    :param token: Персональный токен Figma.
    :param file_key: Ключ файла Figma.
    :param pages: Кортеж с названиями фреймов для экспорта.
    :param output_dir: Директория для сохранения PNG-файлов.
    """
    # Проверяем существование шаблонов
    if is_templates_exist(names=pages):
        return True

    # Проверяем существование директории для вывода
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # URL для получения информации о файле
    info_url = f"https://api.figma.com/v1/files/{file_key}"

    # Заголовки для авторизации
    headers = {
        "X-Figma-Token": token
    }

    # Получаем информацию о документе
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(info_url) as response:
            if response.status != 200:
                raise Exception(
                    f"Ошибка при получении информации о файле: {response.status}, {await response.text()}")

            data = await response.json()  # Используем await для получения JSON-ответа

    # Словарь для хранения ID фреймов
    frame_ids = {}

    # Находим ID фреймов по их названиям
    def find_frame_id(node, target_names):
        if "name" in node and node["name"] in target_names:
            frame_ids[node["name"]] = node["id"]
        if "children" in node:
            for child in node["children"]:
                find_frame_id(child, target_names)

    # Ищем ID фреймов
    document = data.get("document", {}).get("children", [])
    find_frame_id({"children": document}, pages)

    # Проверяем, что все фреймы найдены
    missing_pages = set(pages) - set(frame_ids.keys())
    if missing_pages:
        raise Exception(f"Не найдены фреймы: {', '.join(missing_pages)}")

    # URL для экспорта изображений
    export_url = f"https://api.figma.com/v1/images/{file_key}"

    # Формируем параметры для первого запроса
    params = {
        "ids": ",".join(frame_ids.values()),
        "format": "png",
        "scale": 1
    }

    # Получаем ссылки на изображения
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(export_url, params=params) as export_response:
            if export_response.status != 200:
                raise Exception(
                    f"Ошибка при экспорте изображений: {export_response.status}, {await export_response.text()}")

            # Используем await для получения JSON-ответа
            images_data = await export_response.json()

    # Создаем задачи для скачивания изображений
    tasks = []
    for page_name, frame_id in frame_ids.items():
        image_url_suffix = images_data.get("images", {}).get(frame_id)
        if not image_url_suffix:
            logger.warning(f"Изображение для фрейма {page_name} не доступно.")
            continue

        # Полная ссылка на изображение
        image_url = urljoin("https://api.figma.com", image_url_suffix)

        # Создаем задачу для скачивания изображения
        tasks.append(asyncio.create_task(download_image_async(
            image_url, headers, os.path.join(output_dir, f"{page_name}.png"))))

    # Ждем завершения всех задач
    await asyncio.gather(*tasks)  # Используем await для ожидания всех задач
    return True


# Асинхронная функция для скачивания изображения
async def download_image_async(image_url: str, headers: Dict[str, str], file_path: str):
    """
    Асинхронно скачивает изображение и сохраняет его в файл.

    :param image_url: URL изображения.
    :param headers: Заголовки для авторизации.
    :param file_path: Путь для сохранения файла.
    """
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(image_url) as response:
                if response.status != 200:
                    logger.error(
                        f"Не удалось скачать изображение по URL {image_url}. Код ошибки: {response.status}")
                    return

                # Сохраняем изображение
                with open(file_path, "wb") as f:
                    # Используем await для чтения данных
                    while chunk := await response.content.read(1024):
                        f.write(chunk)

                logger.info(f"Фрейм успешно экспортирован как {file_path}")
    except Exception as e:
        logger.error(f"Ошибка при скачивании изображения {image_url}: {e}")


# Функция для запуска асинхронной задачи
def run_export(token: str, file_key: str, pages: tuple, output_dir: str):
    asyncio.run(export_figma_frames_to_png_async(
        token, file_key, pages, output_dir))
