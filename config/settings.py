from pathlib import Path
# Блок с путями размещения файлов
INFO_FILE = Path('logs/info.log')
DEBUG_FILE = Path('logs/debug.log')
ERROR_FILE = Path('logs/error.log')

# Блок с путями для сохраненных координат объектов на страницах
COORDINATES_FILE = Path('constants/coordinates.pkl')

# Блок с путями к шаблонам страниц
TEMPLATES_PATH = Path('assets/page_templates')
HTML_PATH = Path('assets/html_templates')
HTML_TEMPLATES = [('template1.html', 'styles1.css')]
TEXT_PDF_FILES = ['result1.pdf']

# Блок с путями к готовым img страницам
IMG_PATH = Path('assets/output/images')

# Блок с путем к конечному файлу pdf
PDF_PATH = Path('assets/output/pdfs')
