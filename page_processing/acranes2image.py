from constants.classes import FoundObject, ArcanesObject, Font
from loguru import logger
from typing import List, Dict
from PIL import Image, ImageDraw, ImageFont
from collections import defaultdict

# Рефакторинг через defaultdict


def group_objects_by_frame(objects_data: List[FoundObject]) -> Dict[str, List[FoundObject]]:
    """
    Группирует объекты по их фреймам.

    :param objects_data: Список объектов.
    :return: Словарь, где ключ — название фрейма, значение — список объектов этого фрейма.
    """
    frames = defaultdict(
        list)  # Создаем defaultdict со списком как значением по умолчанию

    for obj in objects_data:
        # Автоматически создается список для нового ключа
        frames[obj.frame].append(obj)

    return frames


# Основная функция
def add_text_to_image(image_path: str,
                      output_path: str,
                      objects_data: List[FoundObject],
                      arcana_data: List[ArcanesObject],
                      fonts_mapping: Dict[str, Font]) -> bool:
    """
    Добавляет текстовые данные на изображения.

    :param image_path: Путь к исходному изображению.
    :param output_path: Путь для сохранения страниц.
    :param objects_data: Список объектов с координатами и размерами.
    :param arcana_data: Список данных для вставки.
    :param fonts_mapping: Словарь с параметрами шрифтов.
    """

    # Группируем данные по фреймам с помощью функции group_objects_by_frame
    frames = group_objects_by_frame(objects_data)

    # Создаем словарь для быстрого доступа к данным из arcana_data
    arcana_dict = {(item.frame, item.object_name)                   : item.arcane for item in arcana_data}

    # Обрабатываем каждый фрейм
    for frame_name, frame_objects in frames.items():
        try:
            # Открываем изображение шаблона
            with Image.open(f"{image_path}/{frame_name}.png") as img:
                draw = ImageDraw.Draw(img)

                for obj in frame_objects:
                    # Получаем данные для текущего объекта
                    arcane = arcana_dict.get((obj.frame, obj.object_name))
                    if arcane is None:
                        logger.warning(
                            f"Данные для объекта {obj.object_name} не найдены.")
                        continue

                    # Получаем параметры шрифта
                    font_info = fonts_mapping.get(obj.object_name)
                    if font_info is None:
                        logger.warning(
                            f"Шрифт для объекта {obj.object_name} не найден.")
                        continue

                    # Загружаем шрифт
                    try:
                        font = ImageFont.truetype(
                            font_info.family, font_info.size)
                    except IOError:
                        logger.error(
                            f"Не удалось загрузить шрифт {font_info.family}.")
                        continue

                    # Вычисляем позицию для центрирования текста (используем textbbox)
                    text_bbox = draw.textbbox((0, 0), arcane, font=font)
                    text_width = text_bbox[2] - text_bbox[0]
                    text_height = text_bbox[3] - text_bbox[1]

                    x = obj.x + (obj.width - text_width) / 2
                    y = obj.y + (obj.height - text_height) / 2

                    # Добавляем текст на изображение
                    draw.text((x, y), arcane, fill=font_info.color, font=font,
                              stroke_fill=font_info.stroke_fill, stroke_width=font_info.stroke_width)

                # Сохраняем измененное изображение
                img.save(f"{output_path}/{frame_name[-2:].strip()}.png")
                logger.info(
                    f"Изображение {frame_name} успешно обработано и сохранено.")

        except FileNotFoundError:
            logger.error(f"Файл шаблона {frame_name}.png не найден.")
        except Exception as e:
            logger.error(f"Ошибка при обработке изображения {frame_name}: {e}")

    return True
