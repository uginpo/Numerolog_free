def digital_root(num: int, arcanes_number: int = 9) -> int:
    """Рассчитывает числовой корень из суммы цифр входящего числа.

    Args:
        num (int): исходное число
        arcanes_number (int, optional): Максимальное количество арканов. Defaults to 9.

    Returns:
        int: числовой корень
    """
    number = num

    while number > arcanes_number:
        number = sum_digits(number)

    return number


def sum_digits(n: int) -> int:
    """
    Суммирует цифры числа n.
    """
    return sum(int(d) for d in str(n))
