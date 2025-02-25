from typing import List, Dict
from datetime import date
from loguru import logger

from constants.classes import Client, ArcanesObject, FoundObject
from constants.fields import all_names

from src.calculations.calculator import get_all_arcanes
from src.calculations.fonts_manager import create_fonts_dict


def make_arcanese_for_templates(client_info: Client, coordinates: List[FoundObject]) -> tuple[List[ArcanesObject], Dict]:

    all_arcanes = get_all_arcanes(client_info=client_info)
    fonts_mapping = create_fonts_dict(all_names=all_names)

    return all_arcanes, fonts_mapping
