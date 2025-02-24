from loguru import logger
from pathlib import Path
from config.settings import TEMPLATES_PATH
from constants.fields import pages


def is_templates_exist(names: tuple, figma_token: str, figma_file_key: str) -> bool:
    result = True
    for name in names:
        name = f'{name}.png'
        file_template = TEMPLATES_PATH / name
        result *= file_template.exists()
        logger.info(f'Шаблоны существуют {result}')
    return result
