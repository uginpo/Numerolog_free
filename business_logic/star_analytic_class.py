from typing import NamedTuple, Dict

from text_storage.star_personality_dict import personality_dict
from text_storage.star_spirituality_dict import spirituality_dict
from text_storage.star_money_dict import money_dict


class Star_analytic_dict(NamedTuple):
    """Кортеж словарей для аналитики страницы Звезда

    Args:
        NamedTuple (Dict): словари соответствующих арканов
    """
    personality_dict: Dict = personality_dict
    spirituality_dict: Dict = spirituality_dict
    money_dict: Dict = money_dict
