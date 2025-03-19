from typing import List, Dict

from business_logic.arcanes_classes import Star, Pifagor, Money
from business_logic.star_analytic_class import Star_analytic_dict


from utils.fill_html_pages import get_page_star


def get_star_analytic(star: Star) -> List:
    """Создает страницы для преобразования в pdf файл
    personality, spirituality, money

    Args:
        star (Star): Класс Star, заполненный значениями арканов

    Returns:
        bool: удачно или нет создались страницы
    """
    data_dict: List = []
    for current_dict, title in zip(Star_analytic_dict(), ['Личность', 'Духовность', 'Деньги']):

        match title:
            case 'Личность':
                arcane = star.personality
                if arcane:
                    data_dict.append(current_dict.get(star.personality))

            case 'spirituality':
                pass
            case 'money':
                pass

    return data_dict
