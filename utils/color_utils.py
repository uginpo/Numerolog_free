def hex_to_rgb(hex_color: str) -> tuple:
    """Перевод цвета из формата hex
    в формат rgb

    Args:
        hex_color (str): hex-format

    Raises:
        ValueError: _description_
        ValueError: _description_

    Returns:
        tuple: rgb-format
    """
    # Убираем символ '#' если он есть
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]

    # Проверяем длину hexadecimal-кода
    if len(hex_color) not in [3, 6]:
        raise ValueError(
            "Некорректная длина HEX-кода. Должна быть 3 или 6 символов.")

    # Если используется сокращённый формат (3 символа), разворачиваем его до 6 символов
    if len(hex_color) == 3:
        hex_color = ''.join([c * 2 for c in hex_color])

    try:
        # Преобразуем каждые два символа в десятичное число
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return (r, g, b)
    except ValueError:
        raise ValueError("Некорректный HEX-код.")
