from typing import Dict
from classes.arcanes_classes import Star


def get_star_content(star: Star) -> Dict:
    """Возвращает словарь с данными для заполнения
    html шаблона страницы

    Args:
        client_data (Star): Класс, соответствующий странице

    Returns:
        Dict: Словарь с контентом
    """

    # Форматируем дату в строку "ДД.ММ.ГГГГ"
    formatted_birthdate = star.client_info.birthday.strftime("%d.%m.%Y")

    return {
        "name": star.client_info.name,
        "birthdate": formatted_birthdate,
        "personality": str(star.personality),
        "spirituality": str(star.spirituality),
        "money": str(star.money),
        "relationship": str(star.relationship),
        "health": str(star.health),
        "pat_male_line_err": str(star.pat_male_line_err),
        "mat_male_line_err": str(star.mat_male_line_err),
        "pat_female_line_err": str(star.pat_female_line_err),
        "doom_err": str(star.doom_err),
        "mat_female_line_err": str(star.mat_female_line_err),
        "mission": str(star.mission),
        "foot_personality": str(star.personality),
        "foot_spirituality": str(star.spirituality),
        "foot_money": str(star.money),
        "foot_relationship": str(star.relationship),
        "foot_health": str(star.health),
    }
