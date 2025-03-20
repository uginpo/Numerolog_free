from typing import Dict

from config.settings import SCALE_PX_MM


def get_star_position() -> Dict:
    """Возвращает список координат для страницы Звезда

    Returns:
        Dict: словарь координат (mm)
    """
    scale = SCALE_PX_MM

    coordinates_px = {
        "header_text": (700, -3260),
        "personality": (352, -2028),
        "spirituality": (1136, -2604),
        "money": (1921, -2028),
        "relationship": (1607, -1112),
        "health": (666, 1112),
        "pat_male_line_err": (957, -2012),
        "mat_male_line_err": (1327, -2012),
        "pat_female_line_err": (1430, -1660),
        "doom_err": (1146, -1450),
        "mat_female_line_err": (860, -1660),
        "mission": (1125, -1790),
        "foot_personality": (734, -493),
        "foot_spirituality": (941, -493),
        "foot_money": (1146, -493),
        "foot_relationship": (1343, -493),
        "foot_health": (1546, -493)
    }
    star_positions_mm = {key: (value[0] * scale, (value[1]+3368) * scale)
                         for key, value in coordinates_px.items()}

    return star_positions_mm
