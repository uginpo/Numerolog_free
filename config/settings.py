from pathlib import Path
# Блок с путями размещения файлов
INFO_FILE = Path('logs/info.log')
DEBUG_FILE = Path('logs/debug.log')
ERROR_FILE = Path('logs/error.log')


# Блок с путями к шаблонам страниц и именам шаблонов
TEMPLATES_PATH = Path('assets/html_templates')
TEMPLATE_HTML = 'index.html'
TEMPLATE_IMG = 'img.png'
TEMPLATE_CSS = 'styles.css'
TEMPLATE_JS = 'script.js'


# Блок с путем к конечным файлам - профайлингам pdf
PDF_PATH = Path('output/profiles')
