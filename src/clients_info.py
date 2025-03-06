from datetime import datetime, date
from src.gui.gui_main import enter_data
from classes.arcanes_classes import Client


def get_client_info() -> Client:
    """Обращается к функции ввода имени и ДР клиента

    Returns:
        Client: Имя и ДР Клиента
    """
    client = enter_data()
    return Client(*client)
