from report_storage.report_classes import TextElement, ImagePageData
from typing import Dict, List

from report_storage.configurations.star_position import get_star_position
from report_storage.configurations.star_fonts_colors import get_star_fonts_colors


def generate_star_image_content(page_content: Dict) -> List:

    star_font = get_star_fonts_colors()
    star_position = get_star_position()
    a = star_position
    b = page_content
    c = star_font
    my_list = [TextElement(position=pos, text=text, font=current['font'], color=current['color'])
               for pos, text, current in zip(a.values(), b.values(), c.values())]

    return my_list
