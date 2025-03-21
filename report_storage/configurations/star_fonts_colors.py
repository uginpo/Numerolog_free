from typing import Dict

from utils.color_utils import hex_to_rgb
from config.settings import SCALE_PX_MM


def get_star_fonts_colors() -> Dict:
    """Возвращает список шрифтов с цветом для страницы Звезда

    Returns:
        Dict: словарь шрифтов и цвета
    """

    scale = SCALE_PX_MM
    # Шрифт Ошибок
    size_1 = 220 * scale
    # Шрифт header
    size_2 = 240 * scale
    # Шрифт основных арканов
    size_3 = 280 * scale
    # Шрифт миссии
    size_4 = 300 * scale
    # Шрифт footer
    size_5 = 320 * scale

    # Цвет header, footer
    color1 = hex_to_rgb('#E3DDD0')
    # Цвет основных арканов
    color2 = hex_to_rgb('#E6DFD2')
    # Цвет Ошибок
    color3 = hex_to_rgb('#4E322B')
    # Цвет миссии
    color4 = hex_to_rgb('#FF693A')

    star_fonts_colors = {
        "header_text": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_2},
                        'color': color1},
        "personality": {'font': {'name': 'roboto_bold', 'style': '', 'size': size_3},
                        'color': color2},
        "spirituality": {'font': {'name': 'roboto_bold', 'style': '', 'size': size_3},
                         'color': color2},
        "money": {'font': {'name': 'roboto_bold', 'style': '', 'size': size_3},
                  'color': color2},
        "relationship": {'font': {'name': 'roboto_bold', 'style': '', 'size': size_3},
                         'color': color2},
        "health": {'font': {'name': 'roboto_bold', 'style': '', 'size': size_3},
                   'color': color2},
        "pat_male_line_err": {'font': {'name': 'roboto_medium', 'style': '', 'size': size_1},
                              'color': color3},
        "mat_male_line_err": {'font': {'name': 'roboto_medium', 'style': '', 'size': size_1},
                              'color': color3},
        "pat_female_line_err": {'font': {'name': 'roboto_medium', 'style': '', 'size': size_1},
                                'color': color3},
        "doom_err": {'font': {'name': 'roboto_medium', 'style': '', 'size': size_1},
                     'color': color3},
        "mat_female_line_err": {'font': {'name': 'roboto_medium', 'style': '', 'size': size_1},
                                'color': color3},
        "mission": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_4},
                    'color': color4},
        "foot_personality": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_5},
                             'color': color1},
        "foot_spirituality": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_5},
                              'color': color1},
        "foot_money": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_5},
                       'color': color1},
        "foot_relationship": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_5},
                              'color': color1},
        "foot_health": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_5},
                        'color': color1}
    }

    return star_fonts_colors
