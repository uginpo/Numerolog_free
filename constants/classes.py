from typing import NamedTuple, List
from datetime import date

# Данные клиента при вводе (имя и ДР)


class Client(NamedTuple):
    name: str
    birth_day: date


# Название объекта для поиска координат в figma
class SearchObject(NamedTuple):
    frame: str
    object_name: str


# Найденные объекты с координатами в шаблонах страниц из figma
class FoundObject(NamedTuple):
    frame: str  # Название фрейма
    object_name: str  # Название объекта
    x: float  # Координата x относительно фрейма
    y: float  # Координата y относительно фрейма
    width: float  # Ширина объекта
    height: float  # Высота объекта


# Посчитанные значения арканов
class ArcanesObject(NamedTuple):
    frame: str  # Название фрейма
    object_name: str  # Название объекта
    arcane: str  # Значение аркана

# Данные для 1 страницы "Звезда"


class Main_Objects(NamedTuple):
    object_name: str
    arcane: str
