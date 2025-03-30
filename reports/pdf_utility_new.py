from fpdf import FPDF
from typing import Tuple


class CustomPDF(FPDF):
    def __init__(self, orientation="P", unit="mm", format="A4"):
        super().__init__(orientation=orientation, unit=unit, format=format)
        self._current_background_color = (255, 255, 255)  # По умолчанию белый
        # Флаг, указывающий, что новую страницу нужно залить цветом
        self._needs_background = False

    def add_page(self, orientation=""):
        """Переопределяем add_page, чтобы добавлять заливку при необходимости"""
        super().add_page(orientation)
        if self._needs_background:
            self._fill_page_with_color(self._current_background_color)
            self._needs_background = False  # Сбрасываем флаг

    def _fill_page_with_color(self, color: Tuple[int, int, int]):
        """Заливает текущую страницу цветом"""
        self.set_fill_color(*color)
        self.rect(0, 0, self.w, self.h, 'F')
        self.set_y(10)  # Возвращаем курсор в начало

    def accept_page_break(self):
        """Указываем, что следующая страница должна быть с заливкой"""
        self._needs_background = True
        return True  # Разрешаем разрыв страницы

    def create_text_pages(self, page_data: TextPageData):
        self._current_background_color = page_data.background_color
        self.set_text_color(*page_data.text_color)

        old_title = ''
        for section in page_data.sections:
            if self.y + 20 > self.h - 20:
                self._needs_background = True
                self.add_page()  # Вызовет заливку благодаря переопределённому add_page()

            self.set_font(
                str(section.title_font.get("name")),
                str(section.title_font.get("style")),
                int(section.title_font.get("size"))
            )

            if old_title != section.title:
                old_title = section.title
                self.cell(0, 10, section.title, 0, 1, "C")
                self.ln(5)
                if self.y + 20 > self.h - 20:
                    self._needs_background = True
                    self.add_page()

            if section.subtitle and section.subtitle_font:
                self.set_font(
                    str(section.subtitle_font.get("name")),
                    str(section.subtitle_font.get("style")),
                    int(section.subtitle_font.get("size"))
                )
                self.cell(0, 10, section.subtitle, 0, 1, "C")
                self.ln(2)
                if self.y + 20 > self.h - 20:
                    self._needs_background = True
                    self.add_page()

            self.set_font(
                str(section.info_font.get("name")),
                str(section.info_font.get("style")),
                int(section.info_font.get("size"))
            )

            line_height = self.font_size * 1.5

            for info_item in section.info:
                self.multi_cell(0, line_height, info_item, align="L")
                self.ln(self.font_size * 0.3)

                if self.y + 20 > self.h - 20:
                    self._needs_background = True
                    self.add_page()
            self.ln(5)
