from loguru import logger
from pathlib import Path
from typing import Dict, Any
from config.settings import TEMPLATES_PATH
from constants.fields import pages
import requests
import os
# Добавляем импорт для правильного формирования URL
from urllib.parse import urljoin


def is_templates_exist(names: tuple) -> bool:
    result = True
    for name in names:
        name = f'{name}.png'
        file_template = TEMPLATES_PATH / name
        result *= file_template.exists()
        if result:
            logger.info(f'Шаблон {name} существует')
    return result


def export_figma_frames_to_png(token: str, file_key: str, pages: tuple, output_dir: str) -> bool:
    """
    Экспортирует указанные фреймы из Figma в формат PNG.

    :param token: Персональный токен Figma.
    :param file_key: Ключ файла Figma.
    :param pages: Кортеж с названиями фреймов для экспорта.
    :param output_dir: Директория для сохранения PNG-файлов.
    """

    # Проверяем существовани шаблонов
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
    response = requests.get(info_url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Ошибка при получении информации о файле: {response.status_code}, {response.text}")

    data = response.json()

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

    # Экспортируем фреймы
    frame_ids_list = list(frame_ids.values())
    params: Dict[str, Any] = {
        "ids": ",".join(frame_ids_list),
        "format": "png",
        # Масштаб изображения (можно изменить на 2 или 3 для более высокого разрешения)
        "scale": 1
    }

    # Отправляем запрос для получения ссылок на изображения
    export_response = requests.get(export_url, headers=headers, params=params)
    if export_response.status_code != 200:
        raise Exception(
            f"Ошибка при экспорте изображений: {export_response.status_code}, {export_response.text}")

    images_data = export_response.json().get("images", {})

    # Скачиваем каждое изображение
    for page_name, frame_id in frame_ids.items():
        image_url_suffix = images_data.get(frame_id)
        if not image_url_suffix:
            logger.warning(f"Изображение для фрейма {page_name} не доступно.")
            continue

        # Полная ссылка на изображение
        image_url = urljoin("https://api.figma.com", image_url_suffix)

        # Отправляем запрос для скачивания изображения
        image_response = requests.get(image_url, headers=headers)
        if image_response.status_code != 200:
            logger.error(
                f"Не удалось скачать изображение для фрейма {page_name}. Код ошибки: {image_response.status_code}")
            continue

        # Сохраняем изображение
        file_path = os.path.join(output_dir, f"{page_name}.png")
        with open(file_path, "wb") as f:
            f.write(image_response.content)
        logger.info(f"Фрейм {page_name} успешно экспортирован как {file_path}")

    return True
