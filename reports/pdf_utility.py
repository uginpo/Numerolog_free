from fpdf import FPDF
from dataclasses import dataclass
from typing import List, Dict, Tuple, Union, Literal
from pathlib import Path

from report_storage.report_classes import ImagePageData, TextPageData


# Класс PDF
class CustomPDF(FPDF):
    def __init__(self, orientation="P", unit="mm", format="A4", start_page_for_header_footer=0):
        # Вызываем конструктор родительского класса с указанными параметрами
        super().__init__(orientation=orientation, unit=unit, format=format)

        self.start_page_for_header_footer = start_page_for_header_footer

        # добавление пользовательских шрифтов
        self.add_font('roboto_bold', '',
                      'report_storage/fonts/Roboto Mono Bold for Powerline.ttf', uni=True)
        self.add_font('roboto_medium', '',
                      'report_storage/fonts/Roboto Mono Medium for Powerline.ttf', uni=True)
        self.add_font('roboto_regular', '',
                      'report_storage/fonts/Roboto Mono for Powerline.ttf', uni=True)
        self.add_font('roboto_light', '',
                      'report_storage/fonts/Roboto Mono Light for Powerline.ttf', uni=True)

    def header(self):
        if self.start_page_for_header_footer == 0:
            return
        if self.page_no() >= self.start_page_for_header_footer:
            self.set_font("roboto_regular", "", 12)
            self.cell(0, 10, "Название компании или проекта", 0, 1, "C")
            self.ln(10)

    def footer(self):
        if self.start_page_for_header_footer == 0:
            return
        if self.page_no() >= self.start_page_for_header_footer:
            self.set_y(-15)
            self.set_font("roboto_regular", "", 10)
            self.cell(
                0, 10, f"Страница {self.page_no() - self.start_page_for_header_footer + 1}", 0, 0, "C")

    def create_title_page(self, title: str, author_info: Dict[str, str]):
        self.add_page()
        self.set_font("roboto_regular", "", 24)
        self.cell(0, 20, title, 0, 1, "C")
        self.ln(20)

        self.set_font("roboto_regular", "", 16)
        for key, value in author_info.items():
            self.cell(0, 10, f"{key}: {value}", 0, 1, "C")
        self.ln(20)

    def create_image_page(self, page_data: ImagePageData):
        self.add_page()
        self.image(page_data.image_path, x=0, y=0, w=self.w)

        for text_element in page_data.info_positions:
            # Если font указан, используем его; иначе используем стандартный шрифт
            if text_element.font:
                self.set_font(
                    str(text_element.font["name"]),
                    text_element.font.get("style", ''),  # type: ignore
                    int(text_element.font["size"])
                )
            else:
                # Установка стандартного шрифта
                self.set_font("roboto_regular", "", 12)

            # Если color указан, используем его; иначе используем черный цвет по умолчанию
            if text_element.color:
                self.set_text_color(*text_element.color)
            else:
                # Установка стандартного черного цвета
                self.set_text_color(0, 0, 0)

            # Проверяем, что position и text не являются None
            if text_element.position and text_element.text:
                x, y = text_element.position
                self.set_xy(x, y)
                # Рассчитываем ширину текста
                text_width = self.get_string_width(text_element.text)

            # Выводим текст с динамической шириной ячейки и левым выравниванием
                self.cell(
                    w=text_width,  # Ширина ячейки равна ширине текста
                    h=self.font_size,  # Высота строки равна размеру шрифта
                    txt=text_element.text,  # type: ignore
                    align="L"  # Всегда левое выравнивание
                )

    def create_text_pages(self, page_data: TextPageData):
        for section in page_data.sections:
            self.add_page()

            # Название раздела
            title_font = section.title_font
            self.set_font(str(title_font["name"]),
                          title_font.get("style", ""),  # type: ignore
                          int(title_font["size"]))
            self.cell(0, 10, section.title, 0, 1, "L")
            self.ln(10)

            for subsection in section.subsections:
                # Название подраздела
                subtitle_font = subsection.get(
                    "title_font", {"name": "roboto_regular", "style": "B", "size": 14})
                self.set_font(subtitle_font["name"], str(
                    subtitle_font.get("style", "")), int(subtitle_font["size"]))
                self.cell(0, 10, f"- {subsection['title']}", 0, 1, "L")
                self.ln(5)

                # Информация
                info_font = subsection.get(
                    "info_font", {"name": "roboto_regular", "style": "", "size": 12})
                self.set_font(info_font["name"], str(
                    info_font.get("style", "")), int(info_font["size"]))
                self.multi_cell(0, 10, subsection["info"], align="L")
                self.ln(10)


"""    # Данные для создания PDF
    output_path = "example.pdf"
    title = "Название документа"
    author_info = {
        "Автор": "Иван Иванов",
        "Email": "ivan@example.com",
        "Телефон": "+7 (123) 456-78-90",
    }
    """
