from typing import Dict

from utils.color_utils import hex_to_rgb
from config.settings import SCALE_PX_MM


def get_image_fonts_colors() -> Dict:
    """Возвращает список шрифтов с цветом для страницы Звезда

    Returns:
        Dict: словарь шрифтов и цвета
    """

    scale = SCALE_PX_MM
    # Размер шрифта Ошибок
    size_errors = 220 * scale
    # Размер шрифта header
    size_header = 240 * scale
    # Размер шрифта основных арканов
    size_main_arcanes = 280 * scale
    # Размер шрифта миссии
    size_mission = 300 * scale
    # Размер шрифта footer
    size_footer = 320 * scale

    # Цвет header, footer
    header_footer_color = hex_to_rgb('#E3DDD0')
    # Цвет основных арканов
    main_arcanes_color = hex_to_rgb('#E6DFD2')
    # Цвет Ошибок
    errors_color = hex_to_rgb('#4E322B')
    # Цвет миссии
    mission_color = hex_to_rgb('#FF693A')

    star_fonts_colors = {
        "header_text": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_header},
                        'color': header_footer_color},
        "personality": {'font': {'name': 'roboto_bold', 'style': '', 'size': size_main_arcanes},
                        'color': main_arcanes_color},
        "spirituality": {'font': {'name': 'roboto_bold', 'style': '', 'size': size_main_arcanes},
                         'color': main_arcanes_color},
        "money": {'font': {'name': 'roboto_bold', 'style': '', 'size': size_main_arcanes},
                  'color': main_arcanes_color},
        "relationship": {'font': {'name': 'roboto_bold', 'style': '', 'size': size_main_arcanes},
                         'color': main_arcanes_color},
        "health": {'font': {'name': 'roboto_bold', 'style': '', 'size': size_main_arcanes},
                   'color': main_arcanes_color},
        "pat_male_line_err": {'font': {'name': 'roboto_medium', 'style': '', 'size': size_errors},
                              'color': errors_color},
        "mat_male_line_err": {'font': {'name': 'roboto_medium', 'style': '', 'size': size_errors},
                              'color': errors_color},
        "pat_female_line_err": {'font': {'name': 'roboto_medium', 'style': '', 'size': size_errors},
                                'color': errors_color},
        "doom_err": {'font': {'name': 'roboto_medium', 'style': '', 'size': size_errors},
                     'color': errors_color},
        "mat_female_line_err": {'font': {'name': 'roboto_medium', 'style': '', 'size': size_errors},
                                'color': errors_color},
        "mission": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_mission},
                    'color': mission_color},
        "foot_personality": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_footer},
                             'color': header_footer_color},
        "foot_spirituality": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_footer},
                              'color': header_footer_color},
        "foot_money": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_footer},
                       'color': header_footer_color},
        "foot_relationship": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_footer},
                              'color': header_footer_color},
        "foot_health": {'font': {'name': 'roboto_regular', 'style': '', 'size': size_footer},
                        'color': header_footer_color}
    }

    return star_fonts_colors


def get_text_fonts_colors() -> Dict:
    """Возвращает список шрифтов с цветом для страницы
    описания (аналитики) Звезда
    Returns:
        Dict: Словарь шрифтов и цветов
    """
    scale = SCALE_PX_MM
    # Размер шрифта заголовков
    size_title_text = 240 * scale
    # Размер шрифта подзаголовков
    size_subtitle_text = size_title_text / 1.61
    # Размер шрифта текста
    size_plain_text = size_subtitle_text / 1.2
    # Цвет фона страницы
    background_color = hex_to_rgb('#0C182E')
    # Цвет текста
    text_color = hex_to_rgb('#DDF8F8')
    text_fonts_colors = {
        "background_color": background_color,
        "text_color": text_color,
        "title_text": {'name': 'roboto_regular', 'style': '', 'size': size_title_text},
        "subtitle_text": {'name': 'roboto_regular', 'style': '', 'size': size_subtitle_text},
        "plain_text": {'name': 'roboto_light', 'style': '', 'size': size_plain_text}
    }

    return text_fonts_colors
