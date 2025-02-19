from typing import NamedTuple, List
from constants.fields import ArcanesObject, SearchObject, Client
from constants.fields import target_objects, pages
from datetime import date

from src.calculators.arcanes import get_page_arcanes


def get_all_arcanes(client_info: Client, target_objects: List[SearchObject]) -> List[ArcanesObject]:
    """_summary_

    Args:
        client_info (Client): имя и ДР клиента
        target_objects (List[SearchObject]): список вычисляемых арканов

    Returns:
        List[ArcanesObject]: Список вычисляемы арканов с их значениями
    """

    header_data = (f'{name} {birth_day.strftime("%d.%m.%Y")}',)
    main_data = get_main(birth_day)
    additional_data = get_additional(main_data)
    mission_data = (num_to_single(sum(main_data)),)
    footer_data = main_data

    return a


print(pages)


if __name__ == '__main__':
    client_info = Client(name='Julia', birth_day=date.today())
    print(get_all_arcanes(client_info=client_info, target_objects=target_objects))
