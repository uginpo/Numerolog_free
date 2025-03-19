from typing import Dict, List
from fpdf import FPDF

pdf = FPDF(orientation="P", unit='mm', format="A4")
pdf.set_margins(0, 0)
pdf.add_page()
# full page height, half page width
pdf.image("Additional/image/img.jpg", x=0, y=0, w=pdf.w)

pdf.set_text_color(r=255, b=255, g=255)
pdf.add_font('roboto_medium', '',
             '/Users/user/Library/Fonts/Roboto Mono Medium for Powerline.ttf', uni=True)
pdf.add_font('roboto_regular', '', '/Users/user/Library/Fonts/Roboto Mono for Powerline.ttf',
             uni=True)  # Скачайте этот шрифт, если его нет
pdf.set_font('roboto_regular', '', 20)

pdf.cell(0, 40, f'Это линия')
pdf.output('_star.pdf')


def create_star_report(page_content: Dict, analytic_content: List) -> bool:
    """Создает итоговый отчет в виде pdf файла

    Args:
        page_content (Dict): Содержание для заполнения звезды
        analytic_content (List): Содержание для заполнения страниц аналитика

    Returns:
        bool: успешность завершения
    """

    return False
