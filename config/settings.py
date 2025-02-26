from pathlib import Path
# Блок с путями размещения файлов
INFO_FILE = Path('logs/info.log')
DEBUG_FILE = Path('logs/debug.log')
ERROR_FILE = Path('logs/error.log')

# Блок с путями для сохраненных координат объектов на страницах
COORDINATES_FILE = Path('constants/coordinates.pkl')

# Блок с путями к шаблонам страниц
TEMPLATES_PATH = Path('assets/page_templates')

# Блок с путями к готовым img страницам
IMG_PATH = Path('assets/output/images')

# Блок с путем к конечному файлу pdf
PDF_PATH = Path('/Users/user/PythonProjects/Numerolog_free/assets/output/pdfs')
