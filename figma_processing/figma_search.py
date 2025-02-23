import requests
from typing import NamedTuple, List
import os

from constants.fields import target_objects
from constants.classes import SearchObject, FoundObject


# Функция для рекурсивного поиска объектов
def find_objects(node, target_objects, parent_frame=None) -> List[FoundObject]:
    """
    Рекурсивно ищет объекты из списка target_objects.

    :param node: Текущий узел (страница, фрейм или слой).
    :param target_objects: Список объектов для поиска (именованные кортежи).
    :param parent_frame: Родительский фрейм для вычисления относительных координат.
    :return: Список найденных объектов.
    """
    results = []
    lookup_dict = {item.object_name: item for item in target_objects}

    # Проверяем, является ли текущий узел фреймом
    is_frame = node.get("type") == "FRAME"
    current_frame = node if is_frame else parent_frame

    # Если узел имеет имя и находится в списке целевых объектов
    if "name" in node and any(obj.object_name == node["name"] for obj in target_objects):
        if "absoluteBoundingBox" in node and current_frame:
            bbox = node["absoluteBoundingBox"]
            frame_bbox = current_frame["absoluteBoundingBox"]

            # Вычисляем координаты относительно родительского фрейма
            relative_x = bbox["x"] - frame_bbox["x"]
            relative_y = bbox["y"] - frame_bbox["y"]

            # Добавляем размеры объекта
            width = bbox["width"]
            height = bbox["height"]

            # Создаем именованный кортеж для найденного объекта
            results.append(FoundObject(
                frame=lookup_dict.get(node["name"], None).frame,
                object_name=node["name"],
                x=relative_x,
                y=relative_y,
                width=width,
                height=height
            ))

    # Рекурсивно обходим дочерние элементы
    if "children" in node:
        for child in node["children"]:
            results.extend(find_objects(child, target_objects,
                           current_frame if is_frame else parent_frame))

    return results


# Основная функция для поиска объектов в Figma
def search_figma_objects(token: str, file_key: str, target_objects: List[SearchObject]) -> List[FoundObject]:
    """
    Ищет объекты в Figma-файле и возвращает их характеристики.

    :param token: Персональный токен Figma.
    :param file_key: Ключ файла Figma.
    :param target_objects: Список объектов для поиска (именованные кортежи).
    :return: Список найденных объектов (именованные кортежи).
    """
    # URL для получения информации о файле
    url = f"https://api.figma.com/v1/files/{file_key}"

    # Заголовки для авторизации
    headers = {
        "X-Figma-Token": token
    }

    # Отправляем GET-запрос
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        document = data["document"]

        # Начинаем поиск объектов
        found_objects = find_objects(document, target_objects)

        return found_objects
    else:
        raise Exception(
            f"Ошибка при запросе к API Figma: {response.status_code}, {response.text}")
