from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS  # type: ignore
import os

from typing import List, Dict
from pathlib import Path
from constants.classes import ArcanesObject


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
        output_filename,
        stylesheets=[a4_css, CSS(filename='styles.css')],
        presentational_hints=True
    )

    # Удаляем временный файл
    os.remove(temp_html)

    return True


# Пример использования
if __name__ == "__main__":
    sample_data = {
        "sections": [
            {
                "title": "Личность",
                "number": 1,
                "content": "Текст описания личности..."
            },
            {
                "title": "Духовность",
                "number": 7,
                "content": "Текст о духовности..."
            },
            # ... остальные секции
        ]
    }

    generate_pdf_report(sample_data, 'my_report.pdf')
