from typing import List, Dict
from loguru import logger

from classes.arcanes_classes import Star, Pifagor, Money
from classes.star_analytic_class import Star_analytic_dict

from config.settings import TEMPLATES_PATH

from src.utils.fill_html_pages import get_page_star


def get_star_analitics(star: Star) -> bool:
    """Создает страницы для преобразования в pdf файл
    personality, spirituality, money

    Args:
        star (Star): Класс Star, заполненный значениями арканов

    Returns:
        bool: удачно или нет создались страницы
    """
    for current_dict, name in zip(Star_analytic_dict(), ['personality', 'spirituality', 'money']):

        match name:
            case 'personality':
                data_dict = current_dict.get(star.personality)
                result = get_page_star(
                    page_star_content=data_dict,
                    templates=TEMPLATES_PATH,
                    name='personality'
                )
                logger.debug(f'Аналитика личности {data_dict}')

            case 'spirituality':
                pass
            case 'money':
                pass
    return True
