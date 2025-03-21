from typing import Dict

from config.settings import SCALE_PX_MM


def get_star_position() -> Dict:
    """Возвращает список координат для страницы Звезда

    Returns:
        Dict: словарь координат (mm)
    """
    scale = SCALE_PX_MM

    coordinates_px = {
        "header_text": (850, -3142),
        "personality": (350, -2026),
        "spirituality": (1132, -2600),
        "money": (1916, -2028),
        "relationship": (1610, -1112),
        "health": (660, -1112),
        "pat_male_line_err": (955, -2012),
        "mat_male_line_err": (1325, -2012),
        "pat_female_line_err": (1430, -1660),
        "doom_err": (1144, -1450),
        "mat_female_line_err": (858, -1660),
        "mission": (1125, -1780),
        "foot_personality": (734, -470),
        "foot_spirituality": (941, -470),
        "foot_money": (1146, -470),
        "foot_relationship": (1345, -470),
        "foot_health": (1548, -470)
    }
    star_positions_mm = {key: (value[0] * scale, (value[1]+3395) * scale)
                         for key, value in coordinates_px.items()}

    return star_positions_mm
