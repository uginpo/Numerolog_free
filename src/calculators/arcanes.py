from typing import NamedTuple, List
from constants.fields import ArcanesObject, SearchObject, Client
from constants.fields import target_objects, pages
from datetime import date


def get_page_arcanes(client_info: Client, target_objects: List[SearchObject], page_info: str) -> List[ArcanesObject]:
    """_summary_

    Args:
        target_objects (List[SearchObject]): имена заполняемых полей на странице page_info
        page_info (str): название фрейма Figma соответствующее номеру шаблона страницы

    Returns:
        List[ArcanesObject]: посчитанные арканы для заполнения шаблона страницы
    """
    page_objects = list(filter(lambda item: item.frame ==
                               page_info, target_objects))

    return page_objects


if __name__ == '__main__':
    client_info = Client(name="Jul", birth_day=date.today())
    print(get_page_arcanes(client_info,
          target_objects=target_objects, page_info=pages[0]))
