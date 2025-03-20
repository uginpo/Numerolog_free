from typing import Dict, List
from fpdf import FPDF

from report_storage.star_image_creating import generate_star_image_content


def create_star_report(page_content: Dict, analytic_content: List) -> List:
    """Создает итоговый отчет в виде pdf файла

    Args:
        page_content (Dict): Содержание для заполнения звезды
        analytic_content (List): Содержание для заполнения страниц аналитика

    Returns:
        bool: успешность завершения
    """
    star_image_content = generate_star_image_content(page_content=page_content)

    return star_image_content
