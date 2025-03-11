from typing import Dict
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

import os

from classes.arcanes_classes import Star, Pifagor, Money

from config.settings import TEMPLATE_HTML, TEMPLATE_IMG, TEMPLATE_CSS, TEMPLATE_JS


def get_html_star(page_star_content: Dict, templates: Path) -> bool:
    """_summary_

    Args:
        page_star_content (Dict): Арканы звезды для печати
        templates (Path): путь к шаблонам страницы
        output (Path): путь к файлу отчета (профайлингу)

    Returns:
        bool: успешность создания файла отчета
    """
    html = templates/'star'/TEMPLATE_HTML
    # img = templates/'star'/TEMPLATE_IMG
    # css = templates/'star'/TEMPLATE_CSS

    page_html = templates/'star'/f'{page_star_content["name"]}_star.html'

    result = fill_html_with_data(
        my_html=html,
        output_html=page_html,
        data=page_star_content
    )

    return result


def fill_html_with_data(my_html: Path,
                        output_html: Path,
                        data: Dict
                        ) -> bool:
    """Создает pdf документ с описанием арканов

    Args:
        my_html (str): Путь к исходному html шаблону.
        output_html (str): Путь для сохранения заполненной html страницы.
        data (Dict): Словарь с данными для.

    Returns:
        bool: _description_
    """
    # Настройка Jinja2
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(str(my_html))

    # Рендеринг HTML с данными
    rendered_html = template.render(data)

    # Сохраняем временный HTML-файл
    temp_html = output_html
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    return True
