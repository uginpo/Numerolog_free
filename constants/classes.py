from typing import List, Optional
from datetime import date
from dataclasses import dataclass

# Данные клиента при вводе (имя и ДР)


@dataclass
class Client:
    name: str
    birth_day: date


# Название объекта для поиска координат в figma
@dataclass
class SearchObject:
    frame: str
    object_name: str


# Найденные объекты с координатами в шаблонах страниц из figma
@dataclass
class FoundObject:
    frame: str  # Название фрейма
    object_name: str  # Название объекта
    x: float  # Координата x относительно фрейма
    y: float  # Координата y относительно фрейма
    width: float  # Ширина объекта
    height: float  # Высота объекта


# Посчитанные значения арканов
@dataclass
class ArcanesObject:
    frame: str  # Название фрейма
    object_name: str  # Название объекта
    arcane: str  # Значение аркана


# Шрифты
@dataclass
class Font:
    family: str       # Семейство шрифта
    size: int         # Размер шрифта
    color: str        # Цвет шрифта (в формате HEX)
    stroke_fill: Optional[str] = None  # Цвет обводки (опционально)
    stroke_width: Optional[int] = None  # Ширина обводки (опционально)
