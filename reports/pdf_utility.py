from fpdf import FPDF
from dataclasses import dataclass
from typing import List, Dict, Tuple, Union


# Класс PDF
class CustomPDF(FPDF):
    def __init__(self, start_page_for_header_footer=0):
        super().__init__()
        self.start_page_for_header_footer = start_page_for_header_footer

        # добавление пользовательских шрифтов
        pdf.add_font('roboto_bold', '',
                     'report_storage/fonts/Roboto Mono Bold for Powerline.ttf', uni=True)
        pdf.add_font('roboto_medium', '',
                     'report_storage/fonts/Roboto Mono Medium for Powerline.ttf', uni=True)
        pdf.add_font('roboto_regular', '',
                     'report_storage/fonts/Roboto Mono for Powerline.ttf', uni=True)
        pdf.add_font('roboto_light', '',
                     'report_storage/fonts/Roboto Mono Light for Powerline.ttf', uni=True)

    def header(self):
        if self.start_page_for_header_footer == 0:
            return
        if self.page_no() >= self.start_page_for_header_footer:
            self.set_font("DejaVu", "", 12)
            self.cell(0, 10, "Название компании или проекта", 0, 1, "C")
            self.ln(10)

    def footer(self):
        if self.start_page_for_header_footer == 0:
            return
        if self.page_no() >= self.start_page_for_header_footer:
            self.set_y(-15)
            self.set_font("DejaVu", "", 10)
            self.cell(
                0, 10, f"Страница {self.page_no() - self.start_page_for_header_footer + 1}", 0, 0, "C")

    def create_title_page(self, title: str, author_info: Dict[str, str]):
        self.add_page()
        self.set_font("DejaVu", "B", 24)
        self.cell(0, 20, title, 0, 1, "C")
        self.ln(20)

        self.set_font("DejaVu", "", 16)
        for key, value in author_info.items():
            self.cell(0, 10, f"{key}: {value}", 0, 1, "C")
        self.ln(20)

    def create_image_page(self, page_data: ImagePageData):
        self.add_page()
        self.image(page_data.image_path, x=0, y=0, w=self.w)

        for group in page_data.info_positions:
            group_font = group.group_font
            group_color = group.group_color

            self.set_text_color(*group_color)
            self.set_font(group_font["name"], str(
                group_font.get("style", "")), int(group_font["size"]))

            for text_element in group.texts:
                if text_element.font:
                    self.set_font(
                        text_element.font["name"],
                        str(text_element.font.get("style", "")),
                        int(text_element.font["size"])
                    )
                if text_element.color != group_color:
                    self.set_text_color(*text_element.color)

                x, y = text_element.position
                self.set_xy(x, y)
                self.cell(0, 10, text_element.text) font_height = pdf.font_size

    def create_text_pages(self, page_data: TextPageData):
        for section in page_data.sections:
            self.add_page()

            # Название раздела
            title_font = section.title_font
            self.set_font(title_font["name"], str(
                title_font.get("style", "")), int(title_font["size"]))
            self.cell(0, 10, section.title, 0, 1, "L")
            self.ln(10)

            for subsection in section.subsections:
                # Название подраздела
                subtitle_font = subsection.get(
                    "title_font", {"name": "DejaVu", "style": "B", "size": 14})
                self.set_font(subtitle_font["name"], str(
                    subtitle_font.get("style", "")), int(subtitle_font["size"]))
                self.cell(0, 10, f"- {subsection['title']}", 0, 1, "L")
                self.ln(5)

                # Информация
                info_font = subsection.get(
                    "info_font", {"name": "DejaVu", "style": "", "size": 12})
                self.set_font(info_font["name"], str(
                    info_font.get("style", "")), int(info_font["size"]))
                self.multi_cell(0, 10, subsection["info"], align="L")
                self.ln(10)


def generate_pdf(
    output_path: str,
    title: str,
    author_info: Dict[str, str],
    image_page_data: ImagePageData,
    text_page_data: TextPageData,
    include_title_page: bool = True,
    start_page_for_header_footer: int = 0,
):
    pdf = CustomPDF(start_page_for_header_footer=start_page_for_header_footer)
    pdf.add_font("DejaVu", "", "DejaVuSansCondensed.ttf", uni=True)

    # Создание титульной страницы
    if include_title_page:
        pdf.create_title_page(title, author_info)

    # Создание страницы с изображением
    pdf.create_image_page(image_page_data)

    # Создание страниц с текстом
    pdf.create_text_pages(text_page_data)

    # Сохранение PDF-файла
    pdf.output(output_path)


# Пример использования
if __name__ == "__main__":

    # Генерация PDF
    generate_pdf(
        output_path,
        title,
        author_info,
        image_page_data,
        text_page_data,
        include_title_page=True,
        start_page_for_header_footer=3,
    )

"""    # Данные для создания PDF
    output_path = "example.pdf"
    title = "Название документа"
    author_info = {
        "Автор": "Иван Иванов",
        "Email": "ivan@example.com",
        "Телефон": "+7 (123) 456-78-90",
    }
    """
