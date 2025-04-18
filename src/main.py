#! /usr/bin/env python3.13
from loguru import logger


from business_logic.arcanes_classes import Star, Triangle
from business_logic.analytic_class import StarAnalyticInfo
from business_logic.analytic_class import MoneyAnalyticInfo

from input_module.clients_info import get_client_info
from data_requests.data_combiner import combine_all_data
from reports.pdf_creator import create_star_report
from reports.pdf_creator import create_money_report


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
    logger.info("Старт...")
    client_info = get_client_info(("Gene", "7.12.1963"))
    logger.info(f'Имя и ДР клиента {client_info}')

    # 2. Создание арканов для звезды (star) и (money) по данным клиента.
    star = Star(client_info)
    money = Triangle(star)

    # 3. Подготовка данных для создания страницы звезда и денежного треугольника.
    page_star_content = star.get_all_content()
    page_money_content = money.get_all_content()

    # 4. Подготовка данных для создания страниц аналитики звезды и денежного
    # треугольника.
    page_star_analytic = StarAnalyticInfo(star=star).get_all_sections()
    page_money_analytic = MoneyAnalyticInfo(money=money).get_all_sections()

    # 5. Объединение данных для создания страниц с настройками
    union_star_data = combine_all_data(
        page_star_content, page_star_analytic,
        page_name='star'
    )
    union_money_data = combine_all_data(
        page_money_content, page_money_analytic,
        page_name='money'
    )

    # 6. Создание отчета в виде pdf файлов.
    result_star = create_star_report(union_star_data)
    result_money = create_money_report(union_money_data)

    # Завершение работы программы
    if all([result_star, result_money]):
        logger.info("Программа успешно завершила работу.")
    else:
        logger.info("Файлы не созданы")
        logger.error("Файлы не созданы")


# Точка входа в программу
if __name__ == "__main__":

    from utils.log_utils import configure_logger

    configure_logger()
    main()
