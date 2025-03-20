from typing import Dict
from business_logic.arcanes_classes import Star, Pifagor, Money


def get_star_content(star: Star) -> Dict:
    """Возвращает словарь с данными для заполнения
    html шаблона страницы

    Args:
        star (Star): Класс, соответствующий странице

    Returns:
        Dict: Словарь с контентом
    """

    # Форматируем дату в строку "ДД.ММ.ГГГГ"
    formatted_birthdate = star.client_info.birthday.strftime("%d.%m.%Y")

    return {
        "header_text": f'{star.client_info.name} {formatted_birthdate}',
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


def get_pifagor_content(pifagor: Pifagor) -> Dict:
    """Возвращает словарь с данными для заполнения
    html шаблона страницы

    Args:
        pifagor (Pifagor): Класс, соответствующий странице

    Returns:
        Dict: Словарь с контентом
    """
    if pifagor.before_2000():
        additional = f'{pifagor.pif1} {pifagor.pif2} {pifagor.pif3} {pifagor.pif4}'
    else:
        additional = f'{pifagor.pif1} {pifagor.pif2} {pifagor.pif3} {pifagor.pif4} {pifagor.pif5}'

    return {
        "name": pifagor._NAME,
        "birthdate": f'{pifagor._DAY}.{pifagor._MONTH}.{pifagor._YEAR}',
        "additional_pif": additional,
        "number1": pifagor.number1,
        "number2": pifagor.number2,
        "number3": pifagor.number3,
        "number4": pifagor.number4,
        "number5": pifagor.number5,
        "number6": pifagor.number6,
        "number7": pifagor.number7,
        "number8": pifagor.number8,
        "number9": pifagor.number9,
    }


def get_money_content(money: Money) -> Dict:
    """Возвращает словарь с данными для заполнения
    html шаблона страницы

    Args:
        money (Money): Класс, соответствующий странице

    Returns:
        Dict: Словарь с контентом
    """

    return {
        "number1": money.money,
        "number2": money.mat_vtx,
        "number3": money.pat_vtx,
        "number4": money.mat_male_line_err,
        "number5": money.main_vtx,
        "number6": money.pat_female_line_err,
    }
