from typing import NamedTuple, List
from figma_processing.figma_search import search_figma_objects, load_figma_api
from constants.fields import SearchObject, FoundObject, target_objects
from config.my_keys import FIGMA_TOKEN, FIGMA_FILE_KEY


def get_coords(target_objects: List[SearchObject]) -> List[FoundObject]:
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

    #   Поиск объектов
    return (search_figma_objects(token=FIGMA_TOKEN,
                                 file_key=FIGMA_FILE_KEY, target_objects=target_objects))


if __name__ == '__main__':
    found_objects = get_coords(target_objects=target_objects)

    if found_objects:
        print("Найденные объекты:")
        for obj in found_objects:
            print(f"Frame: {obj.frame}, Object: {obj.object_name}, "
                  f"x: {obj.x}, y: {obj.y}, "
                  f"width: {obj.width}, height: {obj.height}")
