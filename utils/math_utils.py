def digital_root(num: int) -> int:
    """
    Рассчитывает однозначное число из суммы цифр числа num.
    """
    number = num
    while number > 9:
        number = sum_digits(number)

    return number


def sum_digits(n: int) -> int:
    """
    Суммирует цифры числа n.
    """
    return sum(int(d) for d in str(n))
