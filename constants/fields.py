from typing import NamedTuple, List
from datetime import date
from constants.classes import SearchObject


page1 = 'A4 - 1'
page2 = 'A4 - 2'
page3 = 'A4 - 3'
pages = (page1, page2, page3)

names_from_page1 = ['Day', 'Month', 'Year', 'Sum_3', 'Sum_4',
                    'Day_Month', 'Month_Year', 'Year_Sum3', 'Sum3_Sum4', 'Day_Sum4',
                    'Sum_all',
                    'Ellipse 1', 'Ellipse 2', 'Ellipse 3', 'Ellipse 4', 'Ellipse 5',
                    'Имя и дата 1'
                    ]

names_from_page2 = ['Имя и дата 2', 'Number 1', 'Number 2', 'Number 3', 'Number 4',
                    'Number 5', 'Number 6', 'Number 7', 'Number 8', 'Number 9'
                    ]

names_from_page3 = ['top', 'left_bottom', 'left_middle', 'right_middle',
                    'right_bottom', 'middle_bottom'
                    ]

target_objects = [
    # Личность Personality
    SearchObject(frame=page1, object_name='Month'),
    # Духовность Spirituality
    SearchObject(frame=page1, object_name='Day'),
    # Реализация Realisation
    SearchObject(frame=page1, object_name='Year'),
    # Отношения Relations
    SearchObject(frame=page1, object_name='Sum_3'),
    # Здоровье Health
    SearchObject(frame=page1, object_name='Sum_4'),
    # Сумма дня и месяца
    SearchObject(frame=page1, object_name='Day_Month'),
    # Сумма месяца и года
    SearchObject(frame=page1, object_name='Month_Year'),
    # Сумма года с суммой день, месяц, год
    SearchObject(frame=page1, object_name='Year_Sum3'),
    # Сумма предыдущей суммы с кумулятивной суммой
    SearchObject(frame=page1, object_name='Sum3_Sum4'),
    # Сумма кумулятивной суммы с суммой года
    SearchObject(frame=page1, object_name='Day_Sum4'),
    # Сумма пяти основных
    SearchObject(frame=page1, object_name='Sum_all'),
    # Личность Personality
    SearchObject(frame=page1, object_name='Ellipse 1'),
    # Духовность Spirituality
    SearchObject(frame=page1, object_name='Ellipse 2'),
    # Реализация Realisation
    SearchObject(frame=page1, object_name='Ellipse 3'),
    # Отношения Relations
    SearchObject(frame=page1, object_name='Ellipse 4'),
    # Здоровье Health
    SearchObject(frame=page1, object_name='Ellipse 5'),
    # Header на Звезде
    SearchObject(frame=page1, object_name='Имя и дата 1'),
    # Header на матрице Пифагора
    SearchObject(frame=page2, object_name='Имя и дата 2'),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name='Number 1'),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name='Number 2'),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name='Number 3'),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name='Number 4'),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name='Number 5'),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name='Number 6'),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name='Number 7'),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name='Number 8'),
    # Числа на матрице Пифагора
    SearchObject(frame=page2, object_name='Number 9'),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name='top'),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name='left_bottom'),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name='left_middle'),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name='right_middle'),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name='right_bottom'),
    # Числа на денежном треугольнике
    SearchObject(frame=page3, object_name='middle_bottom'),
]
