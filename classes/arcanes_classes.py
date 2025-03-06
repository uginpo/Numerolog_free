from datetime import date
from dataclasses import dataclass

# Данные клиента при вводе (имя и ДР)


@dataclass
class Client:
    name: str
    birthday: date


class Star:
    """Класс Звезда вычисляет и хранит данные для заполнения страницы Звезда
    """

    def __init__(self, client_info: Client) -> None:
        # birthday=datetime.date(1982, 7, 23)
        self.client_info: Client = client_info

        # Рассчет переменных блока Звезды
        self.personality: int = self.digital_root(client_info.birthday.day)
        self.spirituality: int = self.digital_root(client_info.birthday.month)
        self.money: int = self.digital_root(client_info.birthday.year)

        self.relationship: int = self.digital_root(
            self.personality +
            self.spirituality +
            self.money
        )

        self.health: int = self.digital_root(
            self.personality +
            self.spirituality +
            self.money +
            self.relationship
        )

        # Рассчет переменной миссия
        self.mission: int = self.digital_root(
            self.personality +
            self.spirituality +
            self.money +
            self.relationship +
            self.health
        )

        # Рассчет переменных блока ошибок
        # Ошибка отца по мужской линии
        self.pat_male_line_err: int = self.digital_root(
            self.personality +
            self.spirituality
        )

        # Ошибка мамы по мужской линии
        self.mat_male_line_err: int = self.digital_root(
            self.spirituality +
            self.money
        )

        # Ошибка отца по женской линии
        self.pat_female_line_err: int = self.digital_root(
            self.money +
            self.relationship
        )

        # Роковая ошибка
        self.doom_err: int = self.digital_root(
            self.relationship +
            self.health
        )

        # Ошибка мамы по женской линии
        self.mat_female_line_err: int = self.digital_root(
            self.health +
            self.personality
        )

    @staticmethod
    def digital_root(num):
        """Рассчитывает одно число из суммы цифр числа num
        Args:
            num (int): number
        Returns:
            int: one number
        """
        string = str(num)

        while len(string) > 1:
            string = str(sum([int(item) for item in string]))

        return int(string)

    @staticmethod
    def sum_digits(n: int) -> int:
        """Суммирует цифры числа. Нужна проверка на превышение 22 для 
        уровня professional"""

        result = sum(int(d) for d in str(n))
        return result

    def __repr__(self):
        return (
            f"Star для {self.client_info.name} ({self.client_info.birthday}):\n"
            "---------------------\n"
            "Блок Звезды:\n"
            f"  personality: {self.personality}\n"
            f"  spirituality: {self.spirituality}\n"
            f"  money: {self.money}\n"
            f"  relationship: {self.relationship}\n"
            f"  health: {self.health}\n"
            f"  mission: {self.mission}\n\n"
            "Блок Ошибок:\n"
            f"  Ошибка отца (муж. линия): {self.pat_male_line_err}\n"
            f"  Ошибка мамы (муж. линия): {self.mat_male_line_err}\n"
            f"  Ошибка отца (жен. линия): {self.pat_female_line_err}\n"
            f"  Роковая ошибка: {self.doom_err}\n"
            f"  Ошибка мамы (жен. линия): {self.mat_female_line_err}\n"
        )
