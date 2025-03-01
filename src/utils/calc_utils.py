from datetime import date
from typing import List, NamedTuple, Any
from loguru import logger
import random

from constants.classes import Client, ArcanesObject
from constants.fields import names_from_page1, names_from_page2, names_from_page3

from text_storage.all_data_dict import all_arcanes_dict
# утилиты для рассчета данных для первой страницы (звезда)


def num_to_single(num):
    """Рассчитывает одно число из суммы цифр числа num
    Args:
        num (int): number
    Returns:
        int: one number
    """
    string = str(num)

    while len(string) > 1:
        string = str(sum([int(item) for item in string]))

    return int(string)


def get_additional(main_data: list) -> list:
    """Возвращает дополнительные числа, рассчитанными попарно из основных
    Args:
        main_data (list): главные арканы
    Returns:
        list: [day_month, month_year, year_sum3, sum3_sum4, sum4_day]
    """
    temp = main_data[:]
    result = [num_to_single(temp[i]+temp[i+1]) for i in range(len(temp)-1)]
    result.append(num_to_single(temp[0]+temp[-1]))

    return result


def get_pif_additional(birth: date) -> tuple:
    """Рассчитывает и возвращает кортеж из дня рождения и дополнительных чисел 

    Args:
        birth (date): дата рождения в формате date

    Returns:
        tuple: (pif_add_1, pif_add_2, pif_add_4, pif_add_4, pif_add_5)
        четыре или пять дополнительных чисел в зависимости от года рождения
    """
    pif1 = sum([int(item) for item in birth.strftime("%d%m%Y")])
    pif2 = num_to_single(pif1) if pif1 not in (11, 22, 33, 44) else pif1
    pif3 = pif1 - 2 * int(str(birth.day)[0]) if birth.year < 2000 else 19
    pif4 = num_to_single(pif3) if birth.year < 2000 else pif1 + pif3
    pif5 = 0 if birth.year < 2000 else num_to_single(pif4)

    result = ((pif1, pif2, pif3, pif4) if birth.year < 2000
              else (pif1, pif2, pif3, pif4, pif5))

    return result


def get_pif_dict(birth: date, pifagor_additional: list) -> list:
    """Принимает дату рождения и дополнительные числа Пифагора
        возвращает список с количеством цифр в каждом квадрате
        от 1 до 9 квадрата Пифагора

    Args:
        birth (date): ДР
        pif_additional (list): Дополнительные числа

    Returns:
        list: список величин для вставки в матрицу Пифагора
    """
    temp = [f'{birth.strftime("%d%m%Y")}']

    temp.extend(pifagor_additional)
    pifagor_matrix = ''.join(temp)
    my_data = pifagor_matrix
    # my_data = "".join([item for item in pif_additional])
    pif_dict = {i-1: str(i) * my_data.count(str(i)) for i in range(1, 10)}
    pif_data = [val if val else '0' for val in pif_dict.values()]

    return pif_data


def get_content(object_name: str, arcane: int) -> str | None:
    """Возвращает описание аркана

    Args:
        object_name (str): поле аркана
        arcane (int): значение аркана

    Returns:
        str: Описание
    """
    if object_name in all_arcanes_dict:
        information: Any = all_arcanes_dict[object_name][1]
    else:
        return None

    content = information.get(arcane, None)
    random_number = random.randint(0, 3)

    if content:
        return content[random_number]
    else:
        return None


def get_title(object_name: str) -> Any:
    """Возвращает заголовок подраздела для заполнения текстовых
    данных страницы

    Args:
        object_name (str): поле аркана

    Returns:
        str: Название аркана (название подраздела)
    """

    if object_name in all_arcanes_dict:
        title = all_arcanes_dict[object_name][0]
    else:
        title = None

    return title
