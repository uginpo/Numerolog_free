from report_storage.report_classes import TextElement, ImagePageData
from report_storage.report_classes import Section, TextPageData
from typing import Dict, List, Any

from report_storage.configurations.star_position import get_star_position
from report_storage.configurations.star_fonts_colors import get_image_fonts_colors
from report_storage.configurations.star_fonts_colors import get_text_fonts_colors


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
    union_text: TextPageData = combine_star_text_data(text_content)

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
    fonts_list: List | Any = get_image_fonts_colors().values()

    # Получаем значения арканов
    arcanes = image_content.values()

    # объединяем в общий список
    combined_list = [TextElement(position=pos, text=arcane, font=font_dict.get('font'), color=font_dict.get('color'))
                     for pos, arcane, font_dict in zip(positions, arcanes, fonts_list)]

    return combined_list


def combine_star_text_data(text_content: List) -> TextPageData:
    """Объединяет данные аналитики с координатами и шрифтами

    Args:
        text_content (List[Dict]): список словарей с аналитикой

    Returns:
        List: Объединенные данные
    """

    # Получаем шрифты
    fonts_dict: Dict | Any = get_text_fonts_colors()
    # цвета
    background_color: tuple | Any = fonts_dict.get('background_color')
    text_color: tuple | Any = fonts_dict.get('text_color')
    # шрифты
    title_font: Dict | Any = fonts_dict.get('title_text')
    subtitle_font = fonts_dict.get('subtitle_text')
    info_font = fonts_dict.get('plain_text')

    sections: List = []

    # перебор всех словарей Личность, Духовность, Деньги
    for curr_dict in text_content:

        section = Section(
            title=curr_dict.get('title'),
            subtitle=curr_dict.get('subtitle'),
            info=curr_dict.get('info'),
            title_font=title_font,
            subtitle_font=subtitle_font,
            info_font=info_font
        )
        sections.append(section)

    union_text = TextPageData(background_color, text_color, sections=sections)

    return union_text
