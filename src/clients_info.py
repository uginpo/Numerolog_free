from datetime import datetime, date
from loguru import logger
from typing import NamedTuple
from src.gui.gui_main import enter_data
from constants.classes import Client


def get_client_info() -> Client:
    client = enter_data()
    logger.debug(client)
    return Client(*client)


if __name__ == '__main__':
    print(get_client_info())
