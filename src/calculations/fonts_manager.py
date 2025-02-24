from typing import Dict, Optional
from loguru import logger

from constants.fields import all_names
from constants.classes import Font
from constants.fonts import *


# Создание словаря для отображения имен объектов к шрифтам
def create_fonts_dict(all_names: list) -> Dict:
    fonts_mapping: Dict[str, Font] = {}

   # Назначение шрифтов с использованием match-case
    for name in all_names:
        match name:
            case "Day" | "Month" | "Year" | "Sum_3" | "Sum_4":
                fonts_mapping[name] = main_font

            case str() as n if n.startswith("Ellipse"):  # Проверка, начинается ли имя с "Ellipse"
                fonts_mapping[name] = additional_font

            case "Sum_all":
                fonts_mapping[name] = mission_font

            case str() as n if n.startswith("Number"):  # Проверка, начинается ли имя с "Number"
                fonts_mapping[name] = header_font

            case "Имя и дата 1" | "Имя и дата 2":  # headers
                fonts_mapping[name] = header_font

            case "top":  # Специальные случаи
                fonts_mapping[name] = money_main_font

            case 'left_bottom' | 'left_middle' | 'right_middle' | 'right_bottom' | 'middle_bottom':
                fonts_mapping[name] = main_font

    logger.debug(f'Словарь {fonts_mapping} создан')

    return fonts_mapping
# Функция для получения шрифта по имени объекта


def get_font_by_name(object_name: str, fonts_mapping: Dict) -> Optional[Font]:
    """
    Возвращает шрифт для указанного объекта по его имени.

    :param object_name: Имя объекта.
    :return: Экземпляр Font или None, если объект не найден.
    """
    font = fonts_mapping.get(object_name)

    logger.debug(f'Шрифт {font} найден')

    return font
