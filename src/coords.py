from typing import NamedTuple, List
from image_processing.figma_search import search_figma_objects, load_figma_api
from constants.fields import SearchObject, FoundObject, target_objects
from config.my_keys import FIGMA_TOKEN, FIGMA_FILE_KEY

# Загрузка token и file_key из .env
# token, file_key = load_figma_credentials()


def get_coords() -> List[FoundObject]:

    #   Поиск объектов
    return (search_figma_objects(token=FIGMA_TOKEN,
                                 file_key=FIGMA_FILE_KEY, target_objects=target_objects))


if __name__ == '__main__':
    found_objects = get_coords()

    if found_objects:
        print("Найденные объекты:")
        for obj in found_objects:
            print(f"Frame: {obj.frame}, Object: {obj.object_name}, "
                  f"x: {obj.x}, y: {obj.y}, "
                  f"width: {obj.width}, height: {obj.height}")
