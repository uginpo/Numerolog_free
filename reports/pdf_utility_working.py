from fpdf import FPDF
from dataclasses import dataclass
from typing import List, Dict, Tuple, Union, Literal
from pathlib import Path

from report_storage.report_classes import ImagePageData, TextPageData


# Класс PDF
class CustomPDF(FPDF):
    def __init__(self, orientation="P", unit="mm", format="A4"):
        # Вызываем конструктор родительского класса с указанными параметрами
        super().__init__(orientation=orientation, unit=unit, format=format)

        # добавление пользовательских шрифтов
        self.add_font('roboto_bold', '',
                      'report_storage/fonts/Roboto Mono Bold for Powerline.ttf', uni=True)
        self.add_font('roboto_medium', '',
                      'report_storage/fonts/Roboto Mono Medium for Powerline.ttf', uni=True)
        self.add_font('roboto_regular', '',
                      'report_storage/fonts/Roboto Mono for Powerline.ttf', uni=True)
        self.add_font('roboto_light', '',
                      'report_storage/fonts/Roboto Mono Light for Powerline.ttf', uni=True)

    def create_image_page(self, page_data: ImagePageData):
        self.add_page()
        self.image(page_data.image_path, x=0, y=0, w=self.w)

        for text_element in page_data.info_positions:
            # Устанавливаем шрифт
            self.set_font(
                str(text_element.font["name"]),  # type: ignore
                str(text_element.font.get("style", '')),  # type: ignore
                int(text_element.font["size"])  # type: ignore
            )
            # Устанавливаем цвет
            self.set_text_color(*text_element.color)

            # Проверяем, что position и text не являются None
            if text_element.position and text_element.text:
                x, y = text_element.position
                # Рассчитываем ширину текста
                text_width = self.get_string_width(text_element.text)
                text_height = self.font_size

                self._add_centered_text(
                    x=x, y=y,
                    text=text_element.text,
                    text_width=text_width, text_height=text_height)

            else:
                raise ValueError(
                    'Отсутствует текст или координаты для вывода данных')

    def create_text_pages(self, page_data: TextPageData):

        # Установка общего цвета текста
        self.set_text_color(*page_data.text_color)
        self._background_color = page_data.background_color

        old_title = ''
        for section in page_data.sections:
            # Проверяем место на странице перед добавлением заголовка раздела
            if self.y + 20 > self.h - 20:  # Если нет места для нового контента
                # Создаем новую страницу с цветом фона
                self._add_colored_page(page_data.background_color)

            # Устанавливаем шрифт заголовка раздела
            self.set_font(
                str(section.title_font.get("name")),  # type: ignore
                str(section.title_font.get("style")),  # type: ignore
                int(section.title_font.get("size"))  # type: ignore
            )

            if old_title != section.title:
                # Выводим название раздела только если оно не повторяется
                old_title = section.title
                self.cell(0, 10, section.title, 0, 1, "C")
                self.ln(5)  # Отступ после названия раздела
                if self.y + 20 > self.h - 20:  # Если нет места для нового контента
                    #    Создаем новую страницу с цветом фона
                    self._add_colored_page(page_data.background_color)

            # Устанавливаем шрифт подзаголовка
            if section.subtitle and section.subtitle_font:
                self.set_font(
                    str(section.subtitle_font.get("name")),  # type: ignore
                    str(section.subtitle_font.get("style")),  # type: ignore
                    int(section.subtitle_font.get("size"))  # type: ignore
                )
                # Выводим подзаголовок
                self.cell(0, 10, section.subtitle, 0, 1, "C")
                self.ln(2)  # Отступ после подзаголовка
                if self.y + 20 > self.h - 20:  # Если нет места для нового контента
                    # Создаем новую страницу с цветом фона
                    self._add_colored_page(page_data.background_color)

            # Устанавливаем шрифт основного текста
            self.set_font(
                str(section.info_font.get("name")),  # type: ignore
                str(section.info_font.get("style")),  # type: ignore
                int(section.info_font.get("size"))  # type: ignore
            )

            # Уменьшаем интервал между строками
            line_height = self.font_size * 1.5  # Высота строки равна 1.2 от размера шрифта

            # Обработка информации внутри раздела
            for info_item in section.info:
                # Проверяем, достаточно ли места на странице
                # Выводим информацию через multi_cell
                self.multi_cell(0, line_height, info_item, align="L")
                # Отступ между элементами информации
                self.ln(self.font_size * 0.3)

                if self.y + 20 > self.h - 20:  # Если нет места для нового контента
                    # Создаем новую страницу с цветом фона
                    self._add_colored_page(page_data.background_color)
            self.ln(5)

    def _add_colored_page(self, background_color: Tuple[int, int, int]):
        """Создает новую страницу с заданным цветом фона"""
        self.add_page()
        self.set_fill_color(*background_color)
        # Прямоугольник со страницей, заполненный цветом
        self.rect(0, 0, self.w, self.h, 'F')
        self.set_y(10)  # Начинаем с верхней части страницы

    def _add_centered_text(self,
                           x: float, y: float,
                           text: str,
                           text_width: int, text_height: int):
        """
        Выводит текст точно по центру относительно координаты x.

        Args:
            x (float): Центральная координата X.
            y (float): Координата Y, где должен начаться текст.
            text (str): Текст для вывода.
            text_width (int): Ширина текста.

        """
        # Корректируем координату x для центрирования текста
        centered_x = x - (text_width / 2)
        centered_y = y - (text_height / 2)

        # Устанавливаем позицию курсора
        self.set_xy(centered_x, centered_y)

        # Выводим текст
        self.cell(w=text_width, h=self.font_size, txt=text, align="C")
        self.set_xy(self.w, self.h)
