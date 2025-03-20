from fpdf import FPDF
from dataclasses import dataclass
from typing import List, Dict, Tuple, Union

from utils.color_utils import hex_to_rgb


# Определение классов для данных
@dataclass
class TextElement:
    """Описывает один текстовый элемент"""
    position: Tuple[float, float] | None = None  # Координаты (x, y)
    text: str | None = None  # Текст
    font: Dict[str, Union[str, int]] | None = None  # Параметры шрифта
    color: Tuple[int, int, int] | None = None  # Цвет текста (RGB)


@dataclass
class ImagePageData:
    """Описывает данные для страницы с изображением"""
    image_path: str  # Путь к изображению
    info_positions: List[TextGroup]  # Группы текстовых элементов


@dataclass
class Section:
    """Описывает раздел текста"""
    title: str  # Название раздела
    title_font: Dict[str, Union[str, int]]  # Шрифт названия раздела
    # Подразделы
    subsections: List[Dict[str, Union[str, Dict[str, Union[str, int]]]]]


@dataclass
class TextPageData:
    """Описывает данные для страницы с текстом"""
    sections: List[Section]  # Список разделов


""" Данные для страницы с изображением
    text1 = TextElement(position=(50, 100), text="Текст 1")
    text2 = TextElement(
        position=(60, 120),
        text="Текст 2",
        font={"name": "DejaVu", "style": "U", "size": 14},
        color=(0, 0, 255)
    )
    group1 = TextGroup(
        group_font={"name": "DejaVu", "style": "B", "size": 16},
        group_color=(255, 255, 255),
        texts=[text1, text2],
    )
    text3 = TextElement(position=(100, 200), text="Текст 3")
    text4 = TextElement(position=(110, 220), text="Текст 4")
    group2 = TextGroup(
        group_font={"name": "DejaVu", "style": "I", "size": 12},
        group_color=(255, 255, 0),
        texts=[text3, text4],
    )
    image_page_data = ImagePageData(
        image_path="example_image.jpg", info_positions=[group1, group2])
"""

"""
        # Данные для страниц с текстом
    section1 = Section(
        title="Раздел 1",
        title_font={"name": "DejaVu", "style": "B", "size": 20},
        subsections=[
            {
                "title": "Подраздел 1.1",
                "title_font": {"name": "DejaVu", "style": "U", "size": 16},
                "info": "Информация о подразделе 1.1",
                "info_font": {"name": "DejaVu", "style": "I", "size": 12},
            },
            {
                "title": "Подраздел 1.2",
                "title_font": {"name": "DejaVu", "style": "B", "size": 14},
                "info": "Информация о подразделе 1.2",
                "info_font": {"name": "DejaVu", "style": "", "size": 10},
            },
        ],
    )
    section2 = Section(
        title="Раздел 2",
        title_font={"name": "DejaVu", "style": "B", "size": 18},
        subsections=[
            {
                "title": "Подраздел 2.1",
                "title_font": {"name": "DejaVu", "style": "BI", "size": 14},
                "info": "Информация о подразделе 2.1",
                "info_font": {"name": "DejaVu", "style": "", "size": 12},
            },
            {
                "title": "Подраздел 2.2",
                "title_font": {"name": "DejaVu", "style": "U", "size": 12},
                "info": "Информация о подразделе 2.2",
                "info_font": {"name": "DejaVu", "style": "I", "size": 10},
            },
        ],
    )
    text_page_data = TextPageData(sections=[section1, section2])
    """
