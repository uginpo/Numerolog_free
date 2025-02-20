from typing import NamedTuple, List
from constants.classes import ArcanesObject, SearchObject, Client, Main_Objects
from constants.fields import target_objects, pages
from datetime import date
from src.utils.file_utils import get_main_arcanes


def get_all_arcanes(client_info: Client, target_objects: List[SearchObject]) -> List[ArcanesObject]:
    """_summary_

    Args:
        client_info (Client): имя и ДР клиента
        target_objects (List[SearchObject]): список вычисляемых арканов

    Returns:
        List[ArcanesObject]: Список вычисляемы арканов с их значениями
    """

    # Блок формирования арканов для 1 страницы "Звезда"
    header_data = f'{client_info.name} {client_info.birth_day.strftime("%d.%m.%Y")}'
    main_arcanes = get_main_arcanes(client_info)
    # additional_data = get_additional(main_data)
    # mission_data = (num_to_single(sum(main_data)),)
    # footer_data = main_data

    # Блок формирования арканов для 2 матрица Пифагора
    # Блок формирования арканов для 3 страницы "Денежный треугольник"
    return main_arcanes


if __name__ == '__main__':
    client_info = Client(name='Julia', birth_day=date.today())
    data = get_all_arcanes(client_info=client_info,
                           target_objects=target_objects)
    for item in data:
        print(item)
