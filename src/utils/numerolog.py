from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


# Шаблоны и результаты
template_path = '/Users/user/Desktop/Python/Jupiter_Notebook/Numerolog/Page_templates/'
result_path = '/Users/user/Desktop/Python/Jupiter_Notebook/Numerolog/Results/'

# Формирование переменных для добавления на 1 страницу ("звезда")
header_data = (f'{name} {birth_day.strftime("%d.%m.%Y")}',)
main_data = get_main(birth_day)
additional_data = get_additional(main_data)
mission_data = (num_to_single(sum(main_data)),)
footer_data = main_data

# Расчет координат для данных в шаблоне
header_coordinates = get_pos(header_data, (header_width, header_height),
                             img=None, my_font=header_font, coordinates=header_coord)
main_coordinates = get_pos(main_data, (main_width, main_height),
                           img=None, my_font=main_font, coordinates=main_coord)
additional_coordinates = get_pos(additional_data, (additional_width, additional_height),
                                 img=None, my_font=additional_font, coordinates=additional_coord)
mission_coordinates = get_pos(mission_data, (mission_width, mission_height),
                              img=None, my_font=mission_font, coordinates=mission_coord)
footer_coordinates = get_pos(footer_data, (footer_width, footer_height),
                             img=None, my_font=footer_font, coordinates=footer_coord)

img = template_path + 'A4 - 1.png'
with Image.open(img) as im:
    text2star(im, header_data, header_coordinates, my_font=header_font)
    text2star(im, main_data, main_coordinates, my_font=main_font)
    text2star(im, additional_data, additional_coordinates,
              my_font=additional_font)
    text2star(im, mission_data, mission_coordinates, my_font=mission_font)
    first_page = text2star(
        im, footer_data, footer_coordinates, my_font=footer_font)

    first_page.show()
    first_page.save(f'{result_path}{name}_page_01.png')

# конец формирования 1 страницы


# Начало формирования страницы Матрица Пифагора
a = get_pif_additional(birth_day)
header_data = (
    " ".join((birth_day.strftime("%d.%m.%Y"), *tuple(map(str, a[1:])))),)
pifagor_data = get_pif_dict(a)

# Формирование координат для вставки в шаблон Таблица Пифагора
pifagor_coord = matrix_from_grid(
    (pifagor_x, pifagor_y), (pifagor_stepx, pifagor_stepy))
header_coordinates = get_pos(header_data, (header_width, header_height),
                             img=None, my_font=header_font, coordinates=header_coord)
pifagor_coordinates = get_pos(pifagor_data, (pifagor_width, pifagor_height),
                              img=None, my_font=pifagor_font, coordinates=pifagor_coord)

# Формирование изображения
img = template_path + 'A4 - 2.png'
with Image.open(img) as im:
    text2star(im, pifagor_data, pifagor_coordinates, my_font=pifagor_font)
    pifogor_page = text2star(
        im, header_data, header_coordinates, my_font=header_font)

    pifogor_page.show()
    pifogor_page.save(f'{result_path}{name}_page_02.png')

# Начало формирования страницы Денежный треугольник
# Формирование данных для вставки в шаблон Денежный треугольник
my_data = (additional_data[1], main_data[2], additional_data[2])
temp = get_additional(my_data)

money_main_data = (main_data[2],)
money_data = (*temp[:2], additional_data[2], temp[2], additional_data[1])

# Формирование координат для вставки в шаблон Таблица Пифагора
money_main_coordinates = get_pos(money_main_data, (money_main_width, money_main_height),
                                 img=None, my_font=money_main_font, coordinates=money_main_coord)
money_coordinates = get_pos(money_data, (money_width, money_height),
                            img=None, my_font=money_font, coordinates=money_coord)

img = template_path + 'A4 - 3.png'
with Image.open(img) as im:
    text2star(im, money_main_data, money_main_coordinates,
              my_font=money_main_font)
    money_page = text2star(
        im, money_data, money_coordinates, my_font=money_font)

    money_page.show()
    money_page.save(f'{result_path}{name}_page_03.png')
