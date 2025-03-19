from input_module.client_input import enter_data
from business_logic.arcanes_classes import Client


def get_client_info() -> Client:
    """Обращается к функции ввода имени и ДР клиента

    Returns:
        Client: Имя и ДР Клиента
    """
    client = enter_data()
    return Client(*client)
