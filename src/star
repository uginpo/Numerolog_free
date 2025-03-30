#!/Users/user/PythonProjects/Numerolog_free/.venv/bin/python3.13
from loguru import logger
from pathlib import Path
import os


from business_logic.arcanes_classes import Client, Star
from business_logic.analytic_class import StarAnalyticInfo

from input_module.clients_info import get_client_info
from data_requests.data_combiner import combine_all_data
from reports.pdf_creator import create_star_report


# Основная функция программы
@logger.catch
def main():
    """
    Главная функция программы. Выполняет следующие шаги:
    1. Получение данных клиента.
    2. Создание арканов для звезды по данным клиента.
    3. Подготовка данных для создания страницы звезда.
    4. Подготовка данных для создания страниц аналитики звезды.
    5. Объединение данных для создания страниц с настройками 
       (шрифтами, координатами).
    6. Создание отчета в виде pdf файла.
    """
    # Настройка логгера
    # configure_logger()

    # 1. Получение данных клиента
    logger.info("Получение данных клиента...")
    client_info = get_client_info()
    logger.debug(f'Имя и ДР клиента {client_info}')

    # Создание контекста для шаблонов страниц
    logger.info("Создание контента страниц...")

    # 2. Создание арканов для звезды (star) по данным клиента.
    logger.info("Создание контента страницы star")
    client_star = Star(client_info)
    logger.debug(f'{client_star}')

    # 3. Подготовка данных для создания страницы звезда.
    page_star_content = client_star.get_all_content()
    logger.debug(f'{page_star_content}')

    # 4. Подготовка данных для создания страниц аналитики звезды.
    page_star_analytic = StarAnalyticInfo(star=client_star).get_all_sections()

    logger.debug(f'{page_star_analytic}')

    # 5. Объединение данных для создания страниц с настройками
    logger.info("Объединение данных для итогового отчета...")
    union_star_data = combine_all_data(
        page_star_content, page_star_analytic,
        page_name='star'
    )
    logger.debug(f'Объединенные данные {union_star_data}')
    logger.info("Объединение данных завершено")

    # 6. Создание отчета в виде pdf файла.
    result = create_star_report(union_star_data)
    logger.info("Завершение создания страницы star")
    # Завершение создания страницы star

    # Завершение работы программы
    logger.info("Программа успешно завершила работу.")


# Точка входа в программу
if __name__ == "__main__":

    from utils.log_utils import configure_logger

    configure_logger()
    main()
