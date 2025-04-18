from input_module.client_input import enter_data
from business_logic.arcanes_classes import Client
from datetime import datetime, date

from config import globals


def get_client_info(client_data: tuple | None = None) -> Client:
    """Обращается к функции ввода имени и ДР клиента

    Returns:
        Client: Имя и ДР Клиента
    """
    client: tuple = client_data if client_data else enter_data()

    full_name, birthday = client
    birthday = birthday if isinstance(
        birthday, date) else datetime.strptime(birthday, '%d.%m.%Y').date()

    # Если имя > 10 символов - в выводе на страницы оставляем только имя
    name = full_name.strip() if len(
        full_name) <= 10 else full_name.strip().split(' ')[0]

    globals.CLIENT_FULL_NAME = f'{full_name.strip()} {birthday.strftime("%d.%m.%Y")}'

    return Client(name=name, birthday=birthday)
