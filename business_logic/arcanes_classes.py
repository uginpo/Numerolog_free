from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Dict

from utils.math_utils import digital_root, sum_digits


# Данные клиента при вводе (имя и дата рождения)
@dataclass
class Client:
    name: str
    birthday: date

    def __post_init__(self):
        if not isinstance(self.birthday, date):
            raise ValueError("Поле birthday должно быть типа datetime.date")
        if self.birthday > date.today():
            raise ValueError("Дата рождения не может быть больше текущей даты")


# Класс для расчета данных звезды
class Star:
    def __init__(self, client_info: Client) -> None:
        self.client_info: Client = client_info

        # Базовые переменные блока Звезды
        self._personality: int = digital_root(client_info.birthday.day)
        self._spirituality: int = digital_root(client_info.birthday.month)
        self._money: int = digital_root(client_info.birthday.year)

    @property
    def personality(self) -> int:
        return self._personality

    @property
    def spirituality(self) -> int:
        return self._spirituality

    @property
    def money(self) -> int:
        return self._money

    @property
    def relationship(self) -> int:
        return digital_root(self.personality + self.spirituality + self.money)

    @property
    def health(self) -> int:
        return digital_root(self.personality + self.spirituality + self.money + self.relationship)

    @property
    def mission(self) -> int:
        return digital_root(self.personality + self.spirituality + self.money + self.relationship + self.health)

    @property
    def foot_personality(self) -> int:
        return digital_root(self.client_info.birthday.day, arcanes_number=9)

    @property
    def foot_spirituality(self) -> int:
        return digital_root(self.client_info.birthday.month, arcanes_number=9)

    @property
    def foot_money(self) -> int:
        return digital_root(self.client_info.birthday.year, arcanes_number=9)

    @property
    def foot_relationship(self) -> int:
        return digital_root(self.personality + self.spirituality + self.money, arcanes_number=9)

    @property
    def foot_health(self) -> int:
        return digital_root(self.personality + self.spirituality + self.money + self.relationship, arcanes_number=9)

    @property
    def pat_male_line_err(self) -> int:
        return digital_root(self.personality + self.spirituality)

    @property
    def mat_male_line_err(self) -> int:
        return digital_root(self.spirituality + self.money)

    @property
    def pat_female_line_err(self) -> int:
        return digital_root(self.money + self.relationship)

    @property
    def doom_err(self) -> int:
        return digital_root(self.relationship + self.health)

    @property
    def mat_female_line_err(self) -> int:
        return digital_root(self.health + self.personality)

    def get_all_content(self) -> Dict:
        """Возвращает словарь со всеми данными для страницы звезда
        """
        formatted_birthdate = self.client_info.birthday.strftime("%d.%m.%Y")

        return {
            "header_text": f'{self.client_info.name} {formatted_birthdate}',
            "personality": str(self.personality),
            "spirituality": str(self.spirituality),
            "money": str(self.money),
            "relationship": str(self.relationship),
            "health": str(self.health),
            "mission": str(self.mission),
            "pat_male_line_err": str(self.pat_male_line_err),
            "mat_male_line_err": str(self.mat_male_line_err),
            "pat_female_line_err": str(self.pat_female_line_err),
            "doom_err": str(self.doom_err),
            "mat_female_line_err": str(self.mat_female_line_err),
            "foot_personality": str(self.foot_personality),
            "foot_spirituality": str(self.foot_spirituality),
            "foot_money": str(self.foot_money),
            "foot_relationship": str(self.foot_relationship),
            "foot_health": str(self.foot_health),
        }

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

# Класс для расчета матрицы Пифагора


class Pifagor:
    class PifagorNumbers(Enum):
        PIF1 = "Сумма цифр даты рождения"
        PIF2 = "ДР к одному числу"
        PIF3 = "Уточнение предыдущего"
        PIF4 = "Предыдущее к одному числу"
        PIF5 = "Резервное число для ДР>=2000"

    def __init__(self, star: Star) -> None:
        self._DAY = star.client_info.birthday.day
        self._MONTH = star.client_info.birthday.month
        self._YEAR = star.client_info.birthday.year
        self._NAME = star.client_info.name

        # Блок рассчета дополнительных чисел
        # Сумма всех цифр даты рождения
        birthday_str = star.client_info.birthday.strftime('%d%m%Y')
        self.pif1: int = sum_digits(int(birthday_str))

        # Сводим pif1 к однозначному числу (корню), если это
        # значение не 11, 22, 33, 44
        self.pif2: int = digital_root(
            self.pif1) if self.pif1 not in (11, 22, 33, 44) else self.pif1

        # Из первого числа отнимаем 2*первое не нулевое число
        # дня рождения, если ДР>=2000г, pif3=19
        self.pif3: int = self.pif1 - 2 * \
            int(str(self._DAY)[0]) if self.before_2000() else 19

        # Сводим pif3 к одному числу. Если ДР>=2000 pif1 + pif3
        self.pif4: int = digital_root(
            self.pif3) if self.before_2000() else self.pif1 + self.pif3

        # не равно 0, только если ДР>=2000
        self.pif5: int = 0 if self.before_2000() else digital_root(self.pif4)

        # Общая строка даты рождения + дополнительных чисел
        all_numbers = f'{birthday_str}{self.pif1}{self.pif2}{self.pif3}{self.pif4}{self.pif5}'
        # Блок данных для матрицы Пифагора
        self.number1: str = '1' * all_numbers.count('1')
        self.number2: str = '2' * all_numbers.count('2')
        self.number3: str = '3' * all_numbers.count('3')
        self.number4: str = '4' * all_numbers.count('4')
        self.number5: str = '5' * all_numbers.count('5')
        self.number6: str = '6' * all_numbers.count('6')
        self.number7: str = '7' * all_numbers.count('7')
        self.number8: str = '8' * all_numbers.count('8')
        self.number9: str = '9' * all_numbers.count('9')

    def before_2000(self) -> bool:
        return self._YEAR < 2000

    def __repr__(self):
        return (
            f"Pifagor для {self._NAME} ({self._DAY}.{self._MONTH}.{self._YEAR}):\n"
            "---------------------\n"
            "Блок Дополнительные числа:\n"
            f"  pif1: {self.pif1}\n"
            f"  pif1: {self.pif2}\n"
            f"  pif1: {self.pif3}\n"
            f"  pif1: {self.pif4}\n"
            f"  pif1: {self.pif5}\n"
            "Блок Матрицы Пифагора:\n"
            f"  единицы: {self.number1}\n"
            f"  двойки: {self.number2}\n"
            f"  тройки: {self.number3}\n"
            f"  четверки: {self.number4}\n"
            f"  пятерки: {self.number5}\n"
            f"  шестерки: {self.number6}\n"
            f"  семерки: {self.number7}\n"
            f"  восьмерки: {self.number8}\n"
            f"  девятки: {self.number9}\n"
        )


class Triangle:
    """Класс Money вычисляет и хранит данные для заполнения страницы
    основного и перевернутого треугольника
    """

    def __init__(self, star: Star) -> None:
        self.star = star  # Храним ссылку на объект Star

    # Блок основного треугольника
        self.vertex = self.star.money
        self.mat_vertex = self.star.mat_male_line_err
        self.pat_vertex = self.star.pat_female_line_err

        # Блок перевернутого треугольника
        # Вершина перевернутого треугольника
        self.inv_vertex = digital_root(
            self.mat_vertex +
            self.pat_vertex
        )

        # Материнский род (слева)
        self.inv_mat_vertex = digital_root(
            self.mat_vertex +
            self.vertex
        )

        # Отцовский род (справа)
        self.inv_pat_vertex = digital_root(
            self.pat_vertex +
            self.vertex
        )

    def get_all_content(self) -> Dict:
        """Возвращает словарь со всеми данными для страницы ДТ
        """
        return {
            "vertex": str(self.vertex),
            "mat_vertex": str(self.mat_vertex),
            "pat_vertex": str(self.pat_vertex),
            "inv_vertex": str(self.inv_vertex),
            "inv_mat_vertex": str(self.inv_mat_vertex),
            "inv_pat_vertex": str(self.inv_pat_vertex),
        }

    def __repr__(self):
        return (
            f"Money для {self.star.client_info.name} ({self.star.client_info.birthday}):\n"
            "---------------------\n"
            "Блок Основной треугольник:\n"
            f"  money: {self.vertex}\n"
            f"  mat_male_line_err: {self.mat_vertex:}\n"
            f"  pat_female_line_err: {self.pat_vertex}\n"
            "Блок Перевернутый треугольник:\n"
            f"  Вершина треугольника: {self.inv_vertex}\n"
            f"  Материнский род (слева): {self.inv_mat_vertex}\n"
            f"  Отцовский род (справа): {self.inv_pat_vertex}\n"
        )
