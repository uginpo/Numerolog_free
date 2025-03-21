from report_storage.report_classes import TextElement, ImagePageData
from typing import Dict, List, Any

from report_storage.configurations.star_position import get_star_position
from report_storage.configurations.star_fonts_colors import get_star_fonts_colors


def combine_all_data(image_content: Dict, text_content: List) -> List:
    """Объединяет все данные для создания полного 
    pdf отчета по странице Star

    Args:
        image_content (Dict): данные арканов
        text_content (List): аналитика (описание) данных арканов

    Returns:
        List: Полные данные, включая шрифты и настройки для 
        создания pdf отчета
    """
    # Объединение данных для страницы-изображения star
    union_data: List = combine_star_image_data(image_content)
    union_text: List = combine_star_text_data(text_content)

    return [union_data, union_text]


def combine_star_image_data(image_content: Dict) -> List:
    """Объединяет данные арканов с координатами и шрифтами

    Args:
        image_content (Dict): данные арканов

    Returns:
        List: Объединенные данные
    """

    # Получаем координаты
    positions = get_star_position().values()

    # Получаем шрифты
    fonts_list: List | Any = get_star_fonts_colors().values()

    # Получаем значения арканов
    arcanes = image_content.values()

    # объединяем в общий список
    combined_list = [TextElement(position=pos, text=arcane, font=font_dict.get('font'), color=font_dict.get('color'))
                     for pos, arcane, font_dict in zip(positions, arcanes, fonts_list)]

    return combined_list


def combine_star_text_data(text_content: List) -> List:
    """Объединяет данные аналитики с координатами и шрифтами

    Args:
        image_content (Dict): данные арканов

    Returns:
        List: Объединенные данные
    """

    return []
