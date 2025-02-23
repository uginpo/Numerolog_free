from typing import NamedTuple, List
import pickle
from loguru import logger
from figma_processing.figma_search import search_figma_objects
from constants.fields import target_objects
from constants.classes import SearchObject, FoundObject
from config.settings import COORDINATES_FILE


def get_coordinates(target_objects: List[SearchObject], token: str, file_key: str) -> List[FoundObject]:
    """Находит и возвращает координаты объектов в шаблонах Figma для
    последующей вставки данных по этим координатам

    Returns:
        List[FoundObject]:  frame: str  # Название фрейма
                            object_name: str  # Название объекта
                            x: float  # Координата x относительно фрейма
                            y: float  # Координата y относительно фрейма
                            width: float  # Ширина объекта
                            height: float  # Высота объекта
    """

    if COORDINATES_FILE.exists():
        with open(COORDINATES_FILE, "rb") as file:
            coordinates = pickle.load(file)
        logger.debug('Файл с координатами считан')
    else:
        #   Поиск объектов
        coordinates = search_figma_objects(token=token,
                                           # Запись в файл
                                           file_key=file_key, target_objects=target_objects)
        with open(COORDINATES_FILE, "wb") as file:
            pickle.dump(coordinates, file)
        logger.debug('Файл с координатами успешно создан')

    return coordinates
