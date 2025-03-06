from typing import Dict, List
from dataclasses import dataclass
from datetime import date
from pathlib import Path


PAGE_NAMES = (
    'star', 'star_text', 'pifagor',
    'pifagor_text', 'money', 'money_text'
)
TEMPLATES_PATH = Path('assets/html_templates')
PAGE_TEMPLATES = ('index.html', 'styles.css', 'img.png')
