from typing import Dict
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import base64
import pdfkit  # type: ignore
from loguru import logger

import os

from business_logic.arcanes_classes import Star, Pifagor, Money

from config.settings import STAR_HTML, STAR_PERSONALITY
from config.settings import STAR_IMG
from config.settings import PDF_PATH


def get_page_star(page_star_content: Dict, templates: Path, name: str = 'star') -> bool:
    """_summary_

    Args:
        page_star_content (Dict): Арканы звезды для печати
        templates (Path): путь к шаблонам страницы
        name (str): имя страницы

    Returns:
        bool: успешность создания файла отчета
    """
    match name:
        case 'star':
            html = templates/'star'/STAR_HTML
            img = templates/'star'/STAR_IMG
            page_html = templates/'star' / \
                f'{page_star_content["name"]}_star.html'
            page_pdf = PDF_PATH/f'{page_star_content["name"]}_star.pdf'

        case 'personality':
            html = templates/'star_analytics'/STAR_PERSONALITY
            img = templates/'star_analytics'/STAR_IMG
            page_html = templates/'star_analytics' / \
                f'_personality.html'
            page_pdf = PDF_PATH/f'_personality.pdf'

    temp_html = fill_html_with_data(
        my_html=html,
        output_html=page_html,
        image=img,
        data=page_star_content
    )

    result = get_text_to_pdf(temp_html=temp_html, output=page_pdf)

    return result


def fill_html_with_data(my_html: Path,
                        output_html: Path,
                        image: Path,
                        data: Dict
                        ) -> str:
    """Создает pdf документ с описанием арканов

    Args:
        my_html (str): Путь к исходному html шаблону.
        output_html (str): Путь для сохранения заполненной html страницы.
        data (Dict): Словарь с данными для.

    Returns:
        bool: _description_
    """
    # Чтение и кодирование изображения в Base64
    with open(image, "rb") as img_file:
        image_data = base64.b64encode(img_file.read()).decode('utf-8')

    data['image_base64'] = image_data  # Добавляем в данные для шаблона
    # Настройка Jinja2
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(str(my_html))

    # Рендеринг HTML с данными
    rendered_html = template.render(data)

    # Сохраняем временный HTML-файл
    temp_html = output_html
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    return rendered_html


def get_text_to_pdf(temp_html: str, output: Path) -> bool:

    options = {
        'page-size': 'A4',
        'margin-top': '0',
        'margin-right': '0',
        'margin-bottom': '0',
        'margin-left': '0',
        'encoding': 'UTF-8',
        'no-outline': None,
        'enable-local-file-access': None,
        'disable-smart-shrinking': None,  # Отключаем сжатие
        'zoom': 1.0,  # Задаем масштаб 100%
        'load-error-handling': 'ignore',
        'viewport-size': '2380x3368',  # Указываем размер страницы
        'quiet': '',
        'page-height': '3368px',
        'page-width': '2380px'
    }

    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

    input_path = temp_html
    output_path = output

    try:
        pdfkit.from_string(input=temp_html,
                           output_path=output,
                           options=options,
                           configuration=config,
                           )
    except pdfkit.errors.PDFKitError as e:
        logger.error(f"Ошибка конвертации: {e}")
    except PermissionError:
        logger.error(f"Ошибка: Нет прав на запись в {output_path}")
    except FileNotFoundError:
        logger.error(f"Ошибка: Директория не существует")
    except OSError as e:
        logger.error(f"Системная ошибка: {e.strerror}")

    return True
