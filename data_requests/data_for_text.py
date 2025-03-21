from typing import List, Dict, Any

from business_logic.arcanes_classes import Star, Pifagor, Money
from business_logic.star_analytic_class import Star_analytic_dict


def get_star_analytic(star: Star) -> List:
    """Создает структуру для заполнения страницы с аналитикой по странице star
    Args:
        star (Star): Класс Star, заполненный значениями арканов

    Returns:
        data_lst: список словарей для заполнения страницы аналитики
    """

    for current_dict, title in zip(Star_analytic_dict(), ['Личность', 'Духовность', 'Деньги']):

        match title:
            case 'Личность':

                my_dict: Dict | Any = current_dict.get(star.personality)
                person_dict: Dict = {
                    'Личность': {
                        'Положительные черты:': my_dict["personality_positive"],
                        'Отрицательные черты:': my_dict["personality_negative"],
                        'Рекомендации': my_dict["personality_recommendations"]
                    }
                }

            case 'Духовность':

                spirit_dict: Dict = {
                    'Духовность': {
                        'Программа рода': current_dict.get(star.spirituality)
                    }
                }

            case 'Деньги':

                mon_dict: Dict | Any = current_dict.get(star.money)
                money_dict: Dict = {
                    'Деньги': {
                        'Кем Вы были в прошлой жизни? / Ваше главное число в денежном треугольнике:': mon_dict["main_number"],
                        'Профессии, которые Вам подходят:': mon_dict["professions"],
                        'Ваша энергия:': mon_dict["energy"],
                        'Ваши блоки и ограничения:': mon_dict["restrictions"],
                        'Траты, увеличивающие доход:': mon_dict["costs"],
                    }
                }

    return [person_dict, spirit_dict, money_dict]
