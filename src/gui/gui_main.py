import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def enter_data() -> tuple:
    def validate_date(date_str):
        try:
            # Преобразуем строку в объект datetime, а затем в date
            return datetime.strptime(date_str, '%d.%m.%Y').date()
        except ValueError:
            raise ValueError(
                "Неверный формат даты. Используйте формат dd.mm.yyyy")

    def submit():
        nonlocal result  # Используем переменную result из области видимости enter_data()
        date_str = entry_date.get()
        name = entry_name.get()

        # Проверяем и преобразуем дату
        try:
            date_obj = validate_date(date_str)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
            return

        if not date_obj:
            messagebox.showerror(
                "Ошибка", "Неверный формат даты. Используйте формат dd.mm.yyyy")
            return

        # Сохраняем результат
        result = (name, date_obj)

        # Завершаем работу программы
        root.quit()

    def on_closing():
        root.quit()  # Завершаем работу программы
        root.destroy()  # Уничтожаем окно

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

    # Устанавливаем размер окна и центрируем его
    window_width = 400
    window_height = 150
    center_window(root, window_width, window_height)

    # Обработка события закрытия окна
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Настройка сетки для адаптивного изменения размеров
    root.grid_columnconfigure(1, weight=1)

    # Создание и размещение элементов интерфейса
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

    # Устанавливаем фокус на поле ввода даты при загрузке окна
    entry_date.focus()

    # Привязка обработчиков событий для клавиши Enter
    def on_enter_date(event):
        entry_name.focus()  # Перемещаем фокус на поле ввода имени

    def on_enter_name(event):
        submit_button.focus()  # Перемещаем фокус на кнопку "Отправить"

    def on_enter_submit(event):
        submit()  # Вызываем функцию submit при нажатии Enter на кнопке

    entry_date.bind("<Return>", on_enter_date)  # Enter в поле даты
    entry_name.bind("<Return>", on_enter_name)  # Enter в поле имени
    submit_button.bind("<Return>", on_enter_submit)  # Enter на кнопке

    # Запуск основного цикла обработки событий
    root.mainloop()

    # Возвращаем результат
    if result:
        return result
    else:
        raise ValueError('Не введены данные клиента')


if __name__ == '__main__':
    data = enter_data()
    if data:
        print(data)  # Выводим полученные данные
    else:
        print("Данные не были введены.")
