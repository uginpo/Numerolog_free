from datetime import datetime, date
from typing import NamedTuple
from enter_service import enter_data


class Client(NamedTuple):
    name: str
    birth_day: date


def get_clien_info() -> Client:

    client = enter_data()
    return Client(*client)


if __name__ == '__main__':
    print(get_clien_info())
