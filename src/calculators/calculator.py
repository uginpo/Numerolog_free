from typing import NamedTuple, List
from datetime import date

from constants.classes import ArcanesObject, SearchObject, Client, Main_Objects
from constants.fields import target_objects, pages
from src.utils.pages_utils import get_page1_arcanes, get_page2_arcanes


def get_all_arcanes(client_info: Client) -> List[ArcanesObject]:
    """_summary_

    Args:
        client_info (Client): имя и ДР клиента
        target_objects (List[SearchObject]): список вычисляемых арканов

    Returns:
        List[ArcanesObject]: Список вычисляемы арканов с их значениями
    """

    # Блок формирования арканов для 1 страницы "Звезда"
    main_arcanes = get_page1_arcanes(
        page_num=pages[0], client_info=client_info)

    # Блок формирования арканов для 2 матрица Пифагора
    pifagor_arcanes = get_page2_arcanes(
        page_num=pages[1], client_info=client_info)

    # Блок формирования арканов для 3 страницы "Денежный треугольник"
    money_arcanes = get_page3_arcanes(
        page_num=pages[2], client_info=client_info)

    return pifagor_arcanes


if __name__ == '__main__':
    client_info = Client(name='Julia', birth_day=date.today())
    data = get_all_arcanes(client_info=client_info)
    for item in data:
        print(item)
