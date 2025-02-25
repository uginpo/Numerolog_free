from PIL import Image, ImageDraw, ImageFont
from typing import List, Dict


# Функция для добавления текста на изображение
def add_text_to_image(image_path: str, output_path: str, objects_data: List[FoundObject], arcana_data: List[ArcanesObject], fonts_mapping: Dict[str, Font]):
    """
    Добавляет текстовые данные на изображения.

    :param image_path: Путь к исходному изображению.
    :param output_path: Путь для сохранения измененного изображения.
    :param objects_data: Список объектов с координатами и размерами.
    :param arcana_data: Список данных для вставки.
    :param fonts_mapping: Словарь с параметрами шрифтов.
    """
    # Группируем данные по фреймам
    frames = {}
    for obj in objects_data:
        if obj.frame not in frames:
            frames[obj.frame] = []
        frames[obj.frame].append(obj)

    # Создаем словарь для быстрого доступа к данным из arcana_data
    arcana_dict = {(item.frame, item.object_name): item.arcane for item in arcana_data}

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

                    # Вычисляем позицию для центрирования текста
                    text_width, text_height = draw.textsize(arcane, font=font)
                    x = obj.x + (obj.width - text_width) / 2
                    y = obj.y + (obj.height - text_height) / 2

                    # Добавляем текст на изображение
                    draw.text((x, y), arcane, fill=font_info.color, font=font,
                              stroke_fill=font_info.stroke_fill, stroke_width=font_info.stroke_width)

                # Сохраняем измененное изображение
                img.save(f"{output_path}/{frame_name}_edited.png")
                logger.info(
                    f"Изображение {frame_name} успешно обработано и сохранено.")

        except FileNotFoundError:
            logger.error(f"Файл шаблона {frame_name}.png не найден.")
        except Exception as e:
            logger.error(f"Ошибка при обработке изображения {frame_name}: {e}")


# Пример использования
if __name__ == "__main__":
    # Исходные данные
    objects_data = [
        FoundObject(frame='A4 - 1', object_name='Day', x=279.0,
                    y=1308.0, width=220.0, height=220.0),
        FoundObject(frame='A4 - 1', object_name='Month',
                    x=1056.0, y=740.0, width=220.0, height=220.0),
        FoundObject(frame='A4 - 2', object_name='Number 1',
                    x=268.0, y=849.0, width=480.0, height=312.0),
        # ... остальные объекты ...
    ]

    arcana_data = [
        ArcanesObject(frame='A4 - 1', object_name='Day', arcane='5'),
        ArcanesObject(frame='A4 - 1', object_name='Month', arcane='7'),
        ArcanesObject(frame='A4 - 2', object_name='Number 1', arcane='11'),
        # ... остальные данные ...
    ]

    fonts_mapping = {
        'Day': Font(family='Gilroy-Bold.ttf', size=140, color='#E6DFD2'),
        'Month': Font(family='Gilroy-Bold.ttf', size=140, color='#E6DFD2'),
        'Number 1': Font(family='Gilroy-Semibold.ttf', size=120, color='#E3DDD0'),
        # ... остальные шрифты ...
    }

    # Пути к файлам
    image_path = "templates"  # Папка с шаблонами
    output_path = "output"    # Папка для сохранения результатов

    # Вызов функции
    add_text_to_image(image_path, output_path, objects_data,
                      arcana_data, fonts_mapping)
