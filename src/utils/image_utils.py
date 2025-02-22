from PIL import Image, ImageDraw, ImageFont
import numpy as np
from datetime import date
from typing import List, NamedTuple
from constants.classes import Client, Main_Objects
from constants.fields import names_from_page1, names_from_page2, names_from_page3
# утилиты для рассчета данных для первой страницы (звезда)


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
