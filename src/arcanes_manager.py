from typing import NamedTuple, List
from datetime import date
from loguru import logger

from constants.classes import Client, ArcanesObject, FoundObject
from constants.fields import pages

from src.calculations.calculator import get_all_arcanes
from figma_processing.template_creator import is_templates_exist


def make_arcanese_for_templates(client_info: Client, coordinates: List[FoundObject]) -> List[ArcanesObject]:

    all_arcanes = get_all_arcanes(client_info=client_info)

    return all_arcanes
