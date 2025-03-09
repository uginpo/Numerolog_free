from typing import List, Dict
from classes.arcanes_classes import Star, Pifagor, Money


def get_star_analitics(star: Star, star_dict: Dict) -> List[Dict]:
    star_analytics: List[Dict] = [{}]

    for arcane_name, arcane_dict in star_dict.items():

        section_title, section_dict = arcane_dict
        section_number = getattr(star, arcane_name)
        section_content = section_dict.get(section_number)

        star_analytics.append(
            {
                "section_title": section_title,
                "section_number": str(section_number),
                "section_content": section_content
            }
        )
    return star_analytics
