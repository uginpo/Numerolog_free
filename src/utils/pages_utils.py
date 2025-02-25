from datetime import date
from typing import List, NamedTuple
from constants.classes import Client, ArcanesObject
from constants.fields import names_from_page1, names_from_page2, names_from_page3
from src.utils.calc_utils import num_to_single, get_additional, get_pif_additional
from src.utils.calc_utils import get_pif_dict


def get_page1_arcanes(page_num: str, client_info: Client) -> List[ArcanesObject]:
    """ Возвращает арканы и данный для 1 страницы

    Args:
        page_num (str): Номер страницв = название фрейма
        client_info (Client): Имя и ДР клиента

    Returns:
        List[ArcanesObject]: Именованный список арканов и данных страницы
    """

    # Формирование данных для 1 страницы
    names = names_from_page1[:]
    client_name, birth = client_info.name, client_info.birth_day

    # Рассчет main арканов
    arcanes = [num_to_single(item)
               for item in (birth.day, birth.month, birth.year)]
    for i in range(2):
        arcanes.append(num_to_single(sum(arcanes)))

    main_data = arcanes[:]

    # Рассчет дополнительных арканов
    arcanes.extend(get_additional(main_data=main_data))

    # Рассчет аркана миссии
    mission_data = main_data[:]
    arcanes.append(num_to_single(sum(mission_data)))

    # Рассчет арканов footer данные совпадают с main арканами
    footer_data = main_data[:]
    arcanes.extend(footer_data)

    # Рассчет арканов для header
    arcanes.append(
        f'{client_name} {birth.strftime("%d.%m.%Y")}')

    main_arcanes = [ArcanesObject(frame=page_num, object_name=name, arcane=str(value))
                    for name, value in zip(names, arcanes)]

    return main_arcanes


def get_page2_arcanes(page_num: str, client_info: Client) -> List[ArcanesObject]:
    """ Возвращает арканы и данный для 2 страницы

    Args:
        page_num (str): Номер страницв = название фрейма
        client_info (Client): Имя и ДР клиента

    Returns:
        List[ArcanesObject]: Именованный список арканов и данных страницы
    """

    # Формирование данных для 2 страницы
    names = names_from_page2[:]
    client_name, birth = client_info.name, client_info.birth_day

    # Рассчет арканов для header
    temp = [f'{client_name} {birth.strftime("%d.%m.%Y")}']

    pifagor_additional = list(map(str, get_pif_additional(birth=birth)))
    temp.extend(pifagor_additional)
    pifagor_header = ' '.join(temp)

    arcanes = [pifagor_header]

    # Рассчет арканов для таблицы Пифагора
    pifagor_data = get_pif_dict(
        birth=birth, pifagor_additional=pifagor_additional)

    arcanes.extend(pifagor_data)

    main_arcanes = [ArcanesObject(frame=page_num, object_name=name, arcane=str(value))
                    for name, value in zip(names, arcanes)]

    return main_arcanes


def get_page3_arcanes(page_num: str, client_info: Client) -> List[ArcanesObject]:
    """ Возвращает арканы и данный для 3 страницы

    Args:
        page_num (str): Номер страницв = название фрейма
        client_info (Client): Имя и ДР клиента

    Returns:
        List[ArcanesObject]: Именованный список арканов и данных страницы
    """

    # Формирование данных для 3 страницы
    names = names_from_page3[:]
    client_name, birth = client_info.name, client_info.birth_day

    # Подготовка рассчета арканов
    temp = [num_to_single(item)
            for item in (birth.day, birth.month, birth.year)]
    temp.append(num_to_single(sum(temp)))
    # [Day, Month, Year, Sum3]
    temp_additional = get_additional(temp[1:])
    # [ Month_Year, Year_Sum3, Month_Sum3]

    # Рассчет арканов для денежного треугольника
    top = temp[2]
    left_bottom, right_bottom = temp_additional[0:2]
    left_middle, right_middle, middle_bottom = get_additional(
        [left_bottom, top, right_bottom])

    arcanes = [left_bottom, left_middle, top,
               right_middle, right_bottom, middle_bottom]

    money_arcanes = [ArcanesObject(frame=page_num, object_name=name, arcane=str(value))
                     for name, value in zip(names, arcanes)]

    return money_arcanes
