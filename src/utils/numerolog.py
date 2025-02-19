import tkinter as tk
from tkinter import messagebox
from datetime import datetime
# import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

from my_package import *


# Глобальные переменные для хранения результата
result = None


def validate_date(date_str):
    try:
        # Преобразуем строку в объект datetime, а затем в date
        date_obj = datetime.strptime(date_str, '%d.%m.%Y').date()
        return date_obj
    except ValueError:
        return None


def submit():
    global result
    date_str = entry_date.get()
    name = entry_name.get()

    # Проверяем и преобразуем дату
    date_obj = validate_date(date_str)
    if not date_obj:
        messagebox.showerror(
            "Ошибка", "Неверный формат даты. Используйте формат dd.mm.yyyy")
        return

    # Сохраняем результат в глобальной переменной
    result = (name, date_obj)
    root.quit()  # Завершаем работу программы


def on_closing():
    root.quit()  # Завершаем работу программы
    root.destroy()  # Уничтожаем окно


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Функции для обработки нажатия клавиши Enter


def on_enter_date(event):
    entry_name.focus()  # Перемещаем фокус на поле ввода имени


def on_enter_name(event):
    submit_button.focus()  # Перемещаем фокус на кнопку "Отправить"


def on_enter_submit(event):
    submit()  # Вызываем функцию submit при нажатии Enter на кнопке


# Создание основного окна
root = tk.Tk()
root.title("Ввод данных")

# Устанавливаем размер окна и центрируем его
window_width = 400  # Увеличили ширину окна
window_height = 150
center_window(root, window_width, window_height)

# Обработка события закрытия окна
root.protocol("WM_DELETE_WINDOW", on_closing)

# Настройка сетки для адаптивного изменения размеров
# Столбец с полями ввода будет расширяться
root.grid_columnconfigure(1, weight=1)

# Создание и размещение элементов интерфейса
label_date = tk.Label(root, text="Введите дату (dd.mm.yyyy):")
label_date.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_date = tk.Entry(root)
# Растягиваем поле ввода по ширине
entry_date.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

label_name = tk.Label(root, text="Введите имя:")
label_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_name = tk.Entry(root)
# Растягиваем поле ввода по ширине
entry_name.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

submit_button = tk.Button(root, text="Отправить", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10,
                   sticky="ew")  # Кнопка растягивается по ширине

# Устанавливаем фокус на поле ввода даты при загрузке окна
entry_date.focus()

# Привязка обработчиков событий для клавиши Enter
entry_date.bind("<Return>", on_enter_date)  # Enter в поле даты
entry_name.bind("<Return>", on_enter_name)  # Enter в поле имени
submit_button.bind("<Return>", on_enter_submit)  # Enter на кнопке

# Запуск основного цикла обработки событий
root.mainloop()

# После завершения работы программы проверяем результат
if result:
    name, birth_day = result
else:
    print("Программа завершена без ввода данных.")
    quit()


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
