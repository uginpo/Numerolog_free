from typing import NamedTuple, List
from datetime import date


page1 = 'A4 - 1'
page2 = 'A4 - 2'
page3 = 'A4 - 3'
pages = (page1, page2, page3)


# Названия кортежа и полей для клиента
class Client(NamedTuple):
    name: str
    birth_day: date


# Название объекта для поиска координат в figma
class SearchObject(NamedTuple):
    frame: str
    object_name: str


class FoundObject(NamedTuple):
    frame: str  # Название фрейма
    object_name: str  # Название объекта
    x: float  # Координата x относительно фрейма
    y: float  # Координата y относительно фрейма
    width: float  # Ширина объекта
    height: float  # Высота объекта


class ArcanesObject(NamedTuple):
    frame: str  # Название фрейма
    object_name: str  # Название объекта
    arcane_value: str  # Значение аркана


target_objects = [
    # Личность Personality
    SearchObject(frame=page1, object_name="Month"),
    # Духовность Spirituality
    SearchObject(frame=page1, object_name="Day"),
    # Реализация Realisation
    SearchObject(frame=page1, object_name="Year"),
    # Отношения Relations
    SearchObject(frame=page1, object_name="Sum_3"),
    # Здоровье Health
    SearchObject(frame=page1, object_name="Sum_4"),
    # Сумма дня и месяца
    SearchObject(frame=page1, object_name="Day_Month"),
    # Сумма месяца и года
    SearchObject(frame=page1, object_name="Month_Year"),
    # Сумма года с суммой день, месяц, год
    SearchObject(frame=page1, object_name="Year_Sum3"),
    # Сумма предыдущей суммы с кумулятивной суммой
    SearchObject(frame=page1, object_name="Sum3_Sum4"),
    # Сумма кумулятивной суммы с суммой года
    SearchObject(frame=page1, object_name="Day_Sum4"),
    # Сумма пяти основных
    SearchObject(frame=page1, object_name="Sum_all"),
    # Личность Personality
    SearchObject(frame=page1, object_name="Ellipse 14"),
    # Духовность Spirituality
    SearchObject(frame=page1, object_name="Ellipse 13"),
    # Реализация Realisation
    SearchObject(frame=page1, object_name="Ellipse 12"),
    # Отношения Relations
    SearchObject(frame=page1, object_name="Ellipse 11"),
    # Здоровье Health
    SearchObject(frame=page1, object_name="Ellipse 10"),
    # Header на Звезде
    SearchObject(frame=page1, object_name="Имя и дата 1"),
    # Header на матрице Пифагора
    SearchObject(frame=page2, object_name="Имя и дата 2"),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name="Number 1"),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name="Number 2"),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name="Number 3"),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name="Number 4"),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name="Number 5"),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name="Number 6"),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name="Number 7"),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name="Number 8"),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name="Number 9"),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name="top"),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name="left_middle"),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name="bottom_middle"),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name="right_middle"),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name="right_bottom"),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name="left_bottom"),
]
