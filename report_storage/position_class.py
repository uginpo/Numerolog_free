from typing import Dict, Tuple

from config.settings import SCALE_PX_MM


class BasePositions:
    """Базовый класс для хранения и преобразования координат"""

    def __init__(self, coordinates_px: Dict, scale: float = SCALE_PX_MM):
        self.scale = scale
        self._coordinates_px = coordinates_px

    @property
    def positions_mm(self) -> Dict:
        """Преобразует координаты из пикселей в миллиметры"""
        return {key: (value[0] * self.scale, value[1] * self.scale)
                for key, value in self._coordinates_px.items()}

    def get_all_positions(self) -> Dict:
        """Возвращает полный словарь позиций в миллиметрах"""
        return self.positions_mm


class StarPositions(BasePositions):
    """Класс для хранения координат страницы 'Звезда'"""

    def __init__(self, scale: float = SCALE_PX_MM):
        coordinates_px = {
            "header_text": (1190, 296),
            "personality": (412, 1430),
            "spirituality": (1190, 864),
            "money": (1965, 1430),
            "relationship": (1669, 2344),
            "health": (701, 2344),
            "mission": (1190, 1684),
            "pat_male_line_err": (1023, 1430),
            "mat_male_line_err": (1370, 1430),
            "pat_female_line_err": (1464, 1774),
            "doom_err": (1190, 1975),
            "mat_female_line_err": (916, 1774),
            "foot_personality": (781, 2993),
            "foot_spirituality": (985, 2993),
            "foot_money": (1190, 2993),
            "foot_relationship": (1395, 2993),
            "foot_health": (1599, 2993)
        }
        super().__init__(coordinates_px, scale)


class TrianglePositions(BasePositions):
    """Класс для хранения координат страницы 'Треугольник'"""

    def __init__(self, scale: float = SCALE_PX_MM):
        coordinates_px = {
            "vertex": (1190, 1327),
            "mat_vertex": (414, 2856),
            "pat_vertex": (1966, 2856),
            "inv_vertex": (1190, 2856),
            "inv_mat_vertex": (692, 2311),
            "inv_pat_vertex": (1688, 2311)
        }
        super().__init__(coordinates_px, scale)


"""
---------------------------------------------------
Вариант использования
---------------------------------------------------
# Создаем объект StarPositions
star_positions = StarPositions(scale=SCALE_PX_MM)

# Получаем полный словарь позиций в миллиметрах
all_star_positions = star_positions.get_all_positions()

# Выводим все координаты для страницы "Звезда"
print("Координаты для страницы 'Звезда':")
for key, value in all_star_positions.items():
    print(f"  {key}: {value}")

# Создаем объект TrianglePositions
triangle_positions = TrianglePositions(scale=SCALE_PX_MM)

# Получаем полный словарь позиций в миллиметрах
all_triangle_positions = triangle_positions.get_all_positions()

# Выводим все координаты для страницы "Треугольник"
print("Координаты для страницы 'Треугольник':")
for key, value in all_triangle_positions.items():
    print(f"  {key}: {value}")
        """
