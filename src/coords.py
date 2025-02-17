from figma_search import search_figma_objects, load_figma_credentials
from figma_search import SearchObject

# Загрузка token и file_key из .env
token, file_key = load_figma_credentials()

# Список объектов для поиска
target_objects = [
    SearchObject(name="Объект_1"),
    SearchObject(name="Объект_2"),
    SearchObject(name="Объект_3")
]

try:
    # Поиск объектов
    found_objects = search_figma_objects(token, file_key, target_objects)

    # Вывод результатов
    if found_objects:
        print("Найденные объекты:")
        for obj in found_objects:
            print(f"Frame: {obj.frame}, Object: {obj.object_name}, "
                  f"x: {obj.x}, y: {obj.y}, "
                  f"width: {obj.width}, height: {obj.height}")
    else:
        print("Объекты не найдены.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
