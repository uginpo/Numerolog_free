import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date


def validate_date(date_str: str) -> date:
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
    root.title("Нумерологический профайлинг (free)")

    # Настройка размеров главного окна
    main_window_width = 600
    main_window_height = 400
    center_window(root, main_window_width, main_window_height)

    # Добавляем заголовок в верхней части окна
    header_label = tk.Label(
        root,
        text="Нумерологический профайлинг (free)",
        font=("Arial", 16, "bold")
    )
    header_label.pack(pady=20)

    # Создаем фрейм для формы ввода данных
    form_frame = tk.Frame(root, bg="lightgray", padx=20, pady=20)
    # Размещаем фрейм по центру окна
    form_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Переменная для хранения результата
    result = None

    # Создание элементов интерфейса внутри фрейма
    label_date = tk.Label(form_frame, text="Введите дату (dd.mm.yyyy):")
    label_date.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_date = tk.Entry(form_frame)
    entry_date.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    label_name = tk.Label(form_frame, text="Введите имя:")
    label_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_name = tk.Entry(form_frame)
    entry_name.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    submit_button = tk.Button(form_frame, text="Отправить", command=submit)
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
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

    # Проверяем результат
    if result:
        return result
    else:
        raise ValueError('Не введены данные клиента')
