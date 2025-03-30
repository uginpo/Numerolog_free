from typing import Dict
from business_logic.arcanes_classes import Star, Pifagor, Triangle


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
