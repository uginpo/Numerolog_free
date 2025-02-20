from PIL import Image, ImageDraw, ImageFont
import numpy as np
from datetime import date
from typing import List, NamedTuple
from constants.classes import Client, Main_Objects
from constants.fields import names_from_page1, names_from_page2, names_from_page3
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


def get_main_arcanes(client_info: Client) -> List[Main_Objects]:
    """Возвращает основные числа, рассчитанные по дате рождения
    Args:
        birth: (дата рождения) в формате date  
    Returns:
        List[Main_Objects]: (names_from_page1) Именованый кортеж
    """

    # Формирование данных для 1 страницы
    names = names_from_page1
    clien_name, birth = client_info

    # Рассчет main арканов
    arcanes = [num_to_single(item)
               for item in (birth.day, birth.month, birth.year)]
    for i in range(2):
        arcanes.append(num_to_single(sum(arcanes)))

    # Рассчет дополнительных арканов
    arcanes.extend(get_additional(birth))

    # Рассчет аркана миссии
    mission_data = [num_to_single(item)
                    for item in (birth.day, birth.month, birth.year)]
    arcanes.append(num_to_single(sum(mission_data)))

    # Рассчет арканов footer данные совпадают с main арканами
    arcanes.extend(mission_data)

    # Рассчет арканов для header
    arcanes.append(
        f'{client_info.name} {client_info.birth_day.strftime("%d.%m.%Y")}')

    main_arcanes = [Main_Objects(object_name=name, arcane=str(value))
                    for name, value in zip(names, arcanes)]

    return main_arcanes


def get_additional(birth: date) -> list:
    """Возвращает дополнительные числа, рассчитанными попарно из основных
    Args:
        birth (date): ДР в формате date
    Returns:
        list: [day_month, month_year, year_sum3, sum3_sum4, sum4_day]
    """
    temp = [num_to_single(item)
            for item in (birth.day, birth.month, birth.year)]
    result = [num_to_single(temp[i]+temp[i+1]) for i in range(len(temp)-1)]
    result.append(num_to_single(temp[0]+temp[-1]))

    return result


def get_pos(data, dimension, img=None, my_font=None, coordinates=None):
    """Возвращает координаты для ввода данных в объект img
    Args:
        data (tuple): данные для вставки в изображение
        dimension (tuple): (ширина,  высота) изображения
        img (text): ссылка на файл изображения
        my_font (dict): параметры шрифта
        coordinates (np.array): координаты мест вставки на шаблоне страницы

    Returns:
        a (array): координаты для вставки данных data в шаблон страницы
    """

    # Создаем изображение
    im = Image.open(img) if img else Image.new('RGB', dimension, color='white')

    width, height = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font=my_font['family'], size=my_font['size'])
    X = []
    Y = []

    for item in data:
        # Получаем размеры текста с помощью textbbox
        text_bbox = draw.textbbox((0, 0), str(item), font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Вычисляем координаты для выравнивания текста по центру
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        X.append(x)
        Y.append(y)
        a = np.array([X, Y])

    im.close()
    b = coordinates + a
    return [(float(b[0][i]), float(b[1][i])) for i in range(len(b[0]))]


def text2star(im, data, coords, my_font=None):
    """Вывод на экран и добавление данных к изображению
    Args:
        im : открытый объект класса Image (изображение)
        data (list): данные для добавления в изображение
        coords (tuple): координаты для добавления данных в изображение
        my_font (dict): параметры шрифта
    """

    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype(font=my_font['family'], size=my_font['size'])

    for item in zip(data, coords):
        text = item[0]
        place = item[1]
        draw_text.text(
            place,
            str(text),
            font=font,
            fill=(my_font['color']),
            stroke_fill=my_font['stroke_fill'],
            stroke_width=my_font['stroke_width']
        )
    return im


def get_pif_additional(data):
    """Рассчитывает и возвращает кортеж из дня рождения и дополнительных чисел 

    Args:
        data (date): дата рождения в формате date

    Returns:
        tuple: (pif_add_1, pif_add_2, pif_add_4, pif_add_4, pif_add_5)
        четыре или пять дополнительных чисел в зависимости от года рождения
    """
    pif1 = sum([int(item) for item in data.strftime("%d%m%Y")])
    pif2 = num_to_single(pif1) if pif1 not in (11, 22, 33, 44) else pif1
    pif3 = pif1 - 2 * int(str(data.day)[0]) if data.year < 2000 else 19
    pif4 = num_to_single(pif3) if data.year < 2000 else pif1 + pif3
    pif5 = 0 if data.year < 2000 else num_to_single(pif4)

    result = ((int(data.strftime("%d%m%Y")), pif1, pif2, pif3, pif4) if data.year < 2000
              else (int(data.strftime("%d%m%Y")), pif1, pif2, pif3, pif4, pif5))

    return result


def get_pif_dict(data):
    """Принимает дату рождения и дополнительные числа Пифагора
        возвращает словарь с количеством цифр в каждом квадрате

    Args:
        data tuple: кортеж из даты и доп. чисел

    Returns:
        dict: количество цифр от 1 до 9 в каждом квадрате
    """
    my_data = "".join([str(item) for item in data])
    pif_dict = {i-1: str(i) * my_data.count(str(i)) for i in range(1, 10)}
    pif_data = tuple(val if val else '0' for val in pif_dict.values())

    return pif_data


def matrix_from_grid(initial_coord, step_coord):
    """Подсчетывает координаты ячеек сетки по начальным значениям и шагу

    Args:
        initial_coord (tuple): начальные координаты сетки ячеек для текста
        step_coord (tuple): смещения по x y координат ячеек

    Returns:
        array: массив координат ячеек
    """
    x, y = initial_coord
    delta_x, delta_y = step_coord
    a = np.array([[x]*9, [y]*9])
    row_addition = np.array(list(np.arange(3) * delta_y)*3)

    for j in range(3, 6):
        a[0][j] += delta_x

    for j in range(6, 9):
        a[0][j] += 2 * delta_x

    a[1] += row_addition
    return a
