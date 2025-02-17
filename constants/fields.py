from typing import NamedTuple, List
from datetime import date


# Названия кортежа и полей для клиента
class Client(NamedTuple):
    name: str
    birth_day: date


# Название объекта для поиска координат в figma
class SearchObject(NamedTuple):
    name: str


target_objects = [
    SearchObject(name="Month"),         # Личность Personality
    SearchObject(name="Day"),           # Духовность Spirituality
    SearchObject(name="Year"),          # Реализация Realisation
    SearchObject(name="Sum_3"),         # Отношения Relations
    SearchObject(name="Sum_4"),         # Здоровье Health
    SearchObject(name="Day_Month"),     # Сумма дня и месяца
    SearchObject(name="Month_Year"),    # Сумма месяца и года
    SearchObject(name="Year_Sum3"),     # Сумма года с суммой день, месяц, год
    # Сумма предыдущей суммы с кумулятивной суммой
    SearchObject(name="Sum3_Sum4"),
    # Сумма кумулятивной суммы с суммой года
    SearchObject(name="Day_Sum4"),
    SearchObject(name="Sum_all"),       # Сумма пяти основных
    SearchObject(name="Ellipse 14"),    # Личность Personality
    SearchObject(name="Ellipse 13"),    # Духовность Spirituality
    SearchObject(name="Ellipse 12"),    # Реализация Realisation
    SearchObject(name="Ellipse 11"),    # Отношения Relations
    SearchObject(name="Ellipse 10"),    # Здоровье Health
    SearchObject(name="Имя и дата 1"),  # Header на Звезде
    SearchObject(name="Имя и дата 2"),  # Header на матрице Пифагора
    SearchObject(name="Number 1"),      # Числа на матрице Пифагора
    SearchObject(name="Number 2"),      # Числа на матрице Пифагора
    SearchObject(name="Number 3"),      # Числа на матрице Пифагора
    SearchObject(name="Number 4"),      # Числа на матрице Пифагора
    SearchObject(name="Number 5"),      # Числа на матрице Пифагора
    SearchObject(name="Number 6"),      # Числа на матрице Пифагора
    SearchObject(name="Number 7"),      # Числа на матрице Пифагора
    SearchObject(name="Number 8"),      # Числа на матрице Пифагора
    SearchObject(name="Number 9"),      # Числа на матрице Пифагора
    SearchObject(name="top"),           # Числа на денежном треугольнике
    SearchObject(name="left_middle"),   # Числа на денежном треугольнике
    SearchObject(name="bottom_middle"),  # Числа на денежном треугольнике
    SearchObject(name="right_middle"),  # Числа на денежном треугольнике
    SearchObject(name="right_bottom"),  # Числа на денежном треугольнике
    SearchObject(name="left_bottom"),   # Числа на денежном треугольнике
]
