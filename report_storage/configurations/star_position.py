from typing import Dict

from config.settings import SCALE_PX_MM


def get_star_position() -> Dict:
    """Возвращает список координат для страницы Звезда

    Returns:
        Dict: словарь координат (mm)
    """
    scale = SCALE_PX_MM

    coordinates_px = {'header_text': (850, 253),
                      'personality': (350, 1369),
                      'spirituality': (1132, 795),
                      'money': (1916, 1367),
                      'relationship': (1610, 2283),
                      'health': (660, 2283),
                      'pat_male_line_err': (955, 1383),
                      'mat_male_line_err': (1325, 1383),
                      'pat_female_line_err': (1430, 1735),
                      'doom_err': (1144, 1945),
                      'mat_female_line_err': (858, 1735),
                      'mission': (1125, 1615),
                      'foot_personality': (734, 2925),
                      'foot_spirituality': (941, 2925),
                      'foot_money': (1146, 2925),
                      'foot_relationship': (1345, 2925),
                      'foot_health': (1548, 2925)}

    star_positions_mm = {key: (value[0] * scale, value[1] * scale)
                         for key, value in coordinates_px.items()}

    return star_positions_mm
