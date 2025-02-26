from typing import List, Dict
from constants.classes import ArcanesObject, FoundObject, Font

from page_processing.acranes2image import add_text_to_image


def get_pages_img(image_path: str, output_path: str, objects_data: List[FoundObject],
                  arcana_data: List[ArcanesObject], fonts_mapping: Dict[str, Font]) -> bool:
    """Добавляет посчитанные значения арканов в шаблоны страниц

    Args:
        image_path (str): Путь к исходному изображению (шаблону).
        output_path (str): Путь для сохранения страниц.
        objects_data (List[FoundObject]): Список объектов с координатами и размерами.
        arcana_data (List[ArcanesObject]): Список данных для вставки.
        fonts_mapping (Dict[str, Font]): Словарь с параметрами шрифтов.
    Returns:
        bool: Индикатор успешности заполнения страниц.
    """

    result = add_text_to_image(image_path, output_path, objects_data, arcana_data,
                               fonts_mapping)
    return result
