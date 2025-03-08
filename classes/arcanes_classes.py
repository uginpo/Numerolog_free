from datetime import date
from dataclasses import dataclass

# Данные клиента при вводе (имя и ДР)


@dataclass
class Client:
    name: str
    birthday: date


class Star:
    """Класс Star вычисляет и хранит данные для заполнения страницы Звезда
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


class Pifagor:
    """Класс Pifagor вычисляет и хранит данные для заполнения страницы Звезда
    """

    def __init__(self, star: Star) -> None:
        self._DAY = star.client_info.birthday.day
        self._MONTH = star.client_info.birthday.month
        self._YEAR = star.client_info.birthday.year
        self._NAME = star.client_info.name

        # Блок рассчета дополнительных чисел
        # Сумма всех цифр даты рождения
        self.pif1: int = self.sum_digits(
            int(star.client_info.birthday.strftime('%d%m%Y'))
        )
        # Сводим pif1 к однозначному числу (корню), если это
        # значение не 11, 22, 33, 44
        self.pif2: int = star.digital_root(
            self.pif1) if self.pif1 not in (11, 22, 33, 44) else self.pif1

        # Из первого числа отнимаем 2*первое не нулевое число
        # дня рождения, если ДР>=2000г, pif3=19
        self.pif3: int = self.pif1 - 2 * \
            int(str(self._DAY)[0]) if self.before_2000() else 19

        # Сводим pif3 к одному числу. Если ДР>=2000 pif1 + pif3
        self.pif4: int = star.digital_root(
            self.pif3) if self.before_2000() else self.pif1 + self.pif3

        # не равно 0, только если ДР>=2000
        self.pif5: int = 0 if self.before_2000() else star.digital_root(self.pif4)

        # Блок данных для матрицы Пифагора
        string = f'{self._DAY}{self._MONTH}{self._YEAR}{self.pif1}{self.pif2}{self.pif3}{self.pif4}{self.pif5}'
        self.number1: str = self.get_string(string=string, s='1')
        self.number2: str = self.get_string(string=string, s='2')
        self.number3: str = self.get_string(string=string, s='3')
        self.number4: str = self.get_string(string=string, s='4')
        self.number5: str = self.get_string(string=string, s='5')
        self.number6: str = self.get_string(string=string, s='6')
        self.number7: str = self.get_string(string=string, s='7')
        self.number8: str = self.get_string(string=string, s='8')
        self.number9: str = self.get_string(string=string, s='9')

    def before_2000(self) -> bool:
        return self._YEAR < 2000

    @staticmethod
    def get_string(string: str, s: str) -> str:
        """Возвращает подстроку string из символов s
        """
        return s * string.count(s)

    @staticmethod
    def sum_digits(n: int) -> int:
        """Суммирует цифры числа"""
        return sum(int(d) for d in str(n))

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


class Money:
    """Класс Money вычисляет и хранит данные для заполнения страницы
    основного и перевернутого треугольника
    """

    def __init__(self, star: Star) -> None:

        self._DAY = star.client_info.birthday.day
        self._MONTH = star.client_info.birthday.month
        self._YEAR = star.client_info.birthday.year
        self._NAME = star.client_info.name

        # Назначение переменных блока основной треугольник
        self.money: int = star.money
        self.mat_male_line_err: int = star.mat_male_line_err
        self.pat_female_line_err: int = star.pat_female_line_err

        # Рассчет переменных перевернутого треугольника
        # Вершина перевернутого треугольника
        self.main_vtx: int = star.digital_root(
            self.mat_male_line_err +
            self.pat_female_line_err
        )

        # Материнский род (слева)
        self.mat_vtx: int = star.digital_root(
            self.mat_male_line_err +
            self.money
        )

        # Отцовский род (справа)
        self.pat_vtx: int = star.digital_root(
            self.pat_female_line_err +
            self.money
        )

    def __repr__(self):
        return (
            f"Money для {self._NAME} ({self._DAY}.{self._MONTH}.{self._YEAR}):\n"
            "---------------------\n"
            "Блок Основной треугольник:\n"
            f"  money: {self.money}\n"
            f"  mat_male_line_err: {self.mat_male_line_err:}\n"
            f"  pat_female_line_err: {self.pat_female_line_err}\n"
            "Блок Перевернутый треугольник:\n"
            f"  Вершина треугольника: {self.mat_vtx}\n"
            f"  Материнский род (слева): {self.mat_vtx}\n"
            f"  Отцовский род (справа): {self.pat_vtx}\n"
        )
