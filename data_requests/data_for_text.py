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
                person_list: List = [
                    {
                        'title': 'Личность',
                        'subtitle': 'Положительные черты:',
                        'info': my_dict["personality_positive"]
                    },
                    {
                        'title': 'Личность',
                        'subtitle': 'Отрицательные черты:',
                        'info': my_dict["personality_negative"]
                    },
                    {
                        'title': 'Личность',
                        'subtitle': 'Рекомендации:',
                        'info': my_dict["personality_recommendations"]
                    }
                ]

            case 'Духовность':

                spirit_list: List = [
                    {
                        'title': 'Духовность',
                        'subtitle':   'Программа рода:',
                        'info': current_dict.get(star.spirituality)
                    }
                ]

            case 'Деньги':

                mon_dict: Dict | Any = current_dict.get(star.money)
                money_list: List = [
                    {
                        'title': 'Деньги',
                        'subtitle': 'Кем Вы были в прошлой жизни?',
                        'info': mon_dict["main_number"]
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Профессии, которые Вам подходят:',
                        'info': mon_dict["professions"]
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Ваша энергия:',
                        'info': mon_dict["energy"]
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Ваши блоки и ограничения:',
                        'info': mon_dict["restrictions"]
                    },
                    {
                        'title': 'Деньги',
                        'subtitle': 'Траты, увеличивающие доход:',
                        'info': mon_dict["costs"]
                    }
                ]

    return [*person_list, *spirit_list, *money_list]
