import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def validate_date(date_str):
    """Валидация даты."""
    try:
        return datetime.strptime(date_str, '%d.%m.%Y').date()
    except ValueError:
        raise ValueError("Неверный формат даты. Используйте формат dd.mm.yyyy")


def process_input(name: str, date_str: str) -> tuple:
    """
    Обработка введенных данных.
    Возвращает кортеж (name, date_obj) или выбрасывает исключение.
    """
    if not name.strip():
        raise ValueError("Имя не должно быть пустым")
    date_obj = validate_date(date_str)
    return name.strip(), date_obj


def enter_data() -> tuple:
    """
    Создание графического интерфейса для ввода данных.
    Возвращает кортеж (name, date_obj) или выбрасывает исключение.
    """
    def submit():
        nonlocal result
        name = entry_name.get()
        date_str = entry_date.get()

        try:
            # Вызываем бизнес-логику
            result = process_input(name, date_str)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
            return

        # Завершаем работу программы
        root.quit()

    def on_closing():
        root.quit()
        root.destroy()

    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    # Создание основного окна
    root = tk.Tk()
    root.title("Ввод данных")

    # Переменная для хранения результата
    result = None

    # Настройка окна
    window_width = 400
    window_height = 150
    center_window(root, window_width, window_height)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.grid_columnconfigure(1, weight=1)

    # Создание элементов интерфейса
    label_date = tk.Label(root, text="Введите дату (dd.mm.yyyy):")
    label_date.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_date = tk.Entry(root)
    entry_date.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    label_name = tk.Label(root, text="Введите имя:")
    label_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_name = tk.Entry(root)
    entry_name.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    submit_button = tk.Button(root, text="Отправить", command=submit)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

    # Устанавливаем фокус на поле ввода даты
    entry_date.focus()

    # Привязка обработчиков событий для клавиши Enter
    def on_enter_date(event):
        entry_name.focus()  # Перемещаем фокус на поле ввода имени

    def on_enter_name(event):
        submit_button.focus()  # Перемещаем фокус на кнопку "Отправить"

    def on_enter_submit(event):
        submit()  # Вызываем функцию submit при нажатии Enter на кнопке

    entry_date.bind("<Return>", on_enter_date)
    entry_name.bind("<Return>", on_enter_name)
    submit_button.bind("<Return>", on_enter_submit)

    # Запуск основного цикла обработки событий
    root.mainloop()

    # Проверяем результат
    if result:
        return result
    else:
        raise ValueError('Не введены данные клиента')


if __name__ == '__main__':
    try:
        data = enter_data()
        print(data)  # Выводим полученные данные
    except ValueError as e:
        print(f"Ошибка: {e}")
