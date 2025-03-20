from pathlib import Path
# Блок с путями размещения файлов
INFO_FILE = Path('logs/info.log')
DEBUG_FILE = Path('logs/debug.log')
ERROR_FILE = Path('logs/error.log')


"""
    Размеры страницы A4:
В миллиметрах: 210 мм × 297 мм .
В пикселях (если указано): 2380 × 3368 пикселей .
    """
SCALE_PX_MM: float = 0.0882
