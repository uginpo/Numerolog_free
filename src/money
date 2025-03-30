#!/Users/user/PythonProjects/Numerolog_free/.venv/bin/python3.13
from loguru import logger
from pathlib import Path
import os

from business_logic.arcanes_classes import Client, Star, Triangle
from business_logic.analytic_class import MoneyAnalyticInfo

from input_module.clients_info import get_client_info
from data_requests.data_combiner import combine_all_data
from reports.pdf_creator import create_star_report, create_money_report


# Основная функция программы
@logger.catch
def main():
    """
    Главная функция программы. Выполняет следующие шаги:
    1. Получение данных клиента.
    2. Создание арканов для треугольника денег (ТД) по данным клиента.
    3. Подготовка данных для создания страницы ТД.
    4. Подготовка данных для создания страниц аналитики ТД.
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

    # 2. Создание арканов для ТД по данным клиента.
    logger.info("Создание контента страницы ТД")
    star = Star(client_info=client_info)
    client_money = Triangle(star)
    logger.debug(f'Класс money {client_money}')

    # 3. Подготовка данных для создания страницы ТД.
    page_money_content = client_money.get_all_content()
    logger.debug(f'{page_money_content}')

    # 4. Подготовка данных для создания страниц ТД.
    page_money_analytic = MoneyAnalyticInfo(
        money=client_money).get_all_sections()
    logger.debug(f'{page_money_analytic}')

    # 5. Объединение данных для создания страниц с настройками
    logger.info("Объединение данных для итогового отчета...")
    union_money_data = combine_all_data(
        page_money_content, page_money_analytic,
        page_name='money'
    )
    logger.debug(f'Объединенные данные {union_money_data}')
    logger.info("Объединение данных завершено")

    # 6. Создание отчета в виде pdf файла.
    result = create_money_report(union_money_data)
    logger.info("Завершение создания страницы ДТ")
    # Завершение создания страницы star

    # Завершение работы программы
    logger.info("Программа успешно завершила работу.")


# Точка входа в программу
if __name__ == "__main__":
    from utils.log_utils import configure_logger
    configure_logger()
    main()
