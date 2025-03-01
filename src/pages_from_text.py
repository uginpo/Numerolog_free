from typing import List, Dict
from pathlib import Path

from constants.classes import ArcanesObject
from page_processing.text2pdf import generate_pdf_report

from config.settings import HTML_TEMPLATES, TEXT_PDF_FILES
from config.settings import HTML_PATH, PDF_PATH
from text_storage.page_dicts import content_dict, page1_dict


def get_text_data(arcana_data: List[ArcanesObject], num: int) -> Dict:
    """Формирование словаря для заполнения html шаблонов

    Args:
        arcana_data (List[ArcanesObject]): Список всех арканов с описаниями
        num (int): номер графической страницы

    Returns:
        List[Dict]: Словарь для заполнения шаблона
    """
    match num:
        case 1:
            text_data = page1_dict
        case 2:
            pass
        case 3:
            pass

    return [{}]


def get_pdf_from_txt(arcana_data: List[ArcanesObject]) -> bool:
    """Создает страницы с текстом - описанием арканов

    Args:
        html_path (str): Путь к исходному html шаблону.
        output_path (str): Путь для сохранения страниц с текстом в pdf.
        arcana_data (List[ArcanesObject]): Список данных для вставки.
    Returns:
        bool: Индикатор успешности заполнения страниц.
    """
    result = True
    for templates, pdf_file, num in zip(HTML_TEMPLATES, TEXT_PDF_FILES, [1, 2, 3]):
        html, css = templates
        my_html, my_css = HTML_PATH/html, HTML_PATH/css
        my_pdf = PDF_PATH/pdf_file

        text_data = get_text_data(arcana_data=arcana_data, num=num)

        result = generate_pdf_report(my_html=my_html,
                                     my_css=my_css,
                                     my_pdf=my_pdf,
                                     text_data=text_data,
                                     )

    return result
