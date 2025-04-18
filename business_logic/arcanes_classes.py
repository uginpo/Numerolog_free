from dataclasses import dataclass
from datetime import date
from typing import Dict

from utils.math_utils import digital_root


# Данные клиента при вводе (имя и дата рождения)
@dataclass
class Client:
    name: str
    birthday: date

    def __post_init__(self):
        if not isinstance(self.birthday, date):
            raise ValueError("Неправильно введена дата рождения")
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
