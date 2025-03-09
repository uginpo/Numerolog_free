from typing import Dict
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS  # type: ignore
import os

from classes.arcanes_classes import Star, Pifagor, Money

from config.settings import TEMPLATE_HTML, TEMPLATE_IMG, TEMPLATE_CSS, TEMPLATE_JS


def get_pdf_star(page_star_content: Dict, templates: Path, output: Path) -> bool:
    """_summary_

    Args:
        page_star_content (Dict): Арканы звезды для печати
        templates (Path): путь к шаблонам страницы
        output (Path): путь к файлу отчета (профайлингу)

    Returns:
        bool: успешность создания файла отчета
    """
    html = templates/star/TEMPLATE_HTML
    img = templates/star/TEMPLATE_IMG
    css = templates/star/TEMPLATE_CSS

    profiling_file = output/f'{page_star_content["name"]}_star.pdf'

    result = generate_pdf_report(
        my_html=html,
        my_css=css,
        my_pdf=profiling_file,
        text_data=page_star_content
    )
    return result


def generate_pdf_report(my_html: Path,
                        my_css: Path,
                        my_pdf: Path,
                        text_data: Dict
                        ) -> bool:
    """Создает pdf документ с описанием арканов

    Args:
        html_path (str): Путь к исходному html шаблону.
        output_path (str): Путь для сохранения страниц с текстом в pdf.
        arcana_data (List[ArcanesObject]): Список данных для вставки.

    Returns:
        bool: _description_
    """
    # Настройка Jinja2
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # Рендеринг HTML с данными
    rendered_html = template.render(text_data)

    # Сохраняем временный HTML-файл
    temp_html = 'temp_report.html'
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    # CSS для печати
    a4_css = CSS(string='''
        @page {
            size: A4;
            margin: 15mm;
        }
        body {
            font-family: "Arial", sans-serif;
            line-height: 1.6;
        }
        .section {
            page-break-inside: avoid;
        }
    ''')

    # Генерация PDF
    HTML(temp_html).write_pdf(
        my_pdf,
        stylesheets=[a4_css, CSS(filename='styles.css')],
        presentational_hints=True
    )

    # Удаляем временный файл
    os.remove(temp_html)

    return True
