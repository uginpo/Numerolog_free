from pathlib import Path
from typing import Dict, List
from fpdf import FPDF

from config import globals

from config.data_path import TEMPLATES_PATH, STAR_IMG, OUTPUT_PATH
from report_storage.report_classes import ImagePageData, TextPageData
from reports.pdf_utility import CustomPDF


def create_star_report(union_data: List) -> bool:
    """Создает конечный pdf отчет по Звезде

    Args:
        union_data (List): Объединенные данные для отчета

    Returns:
        bool: успешность создания отчета
    """
    output_path = OUTPUT_PATH/f'{globals.CLIENT_ID}_star.pdf'
    image_page_data, text_page_data = union_data

    star_image_content = generate_pdf(
        output_path=output_path,
        image_page_data=image_page_data
    )

    return True


def generate_pdf(
    output_path: Path,
    title: str = '',
    author_info: Dict[str, str] = {},
    image_page_data: ImagePageData | None = None,
    text_page_data: TextPageData | None = None,
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
    if text_page_data:
        pdf.create_text_pages(text_page_data)

    # Сохранение PDF-файла
    pdf.output(output_path)
