def digital_root(num: int) -> int:
    """
    Рассчитывает однозначное число из суммы цифр числа num.
    """
    string = str(num)
    while len(string) > 1:
        string = str(sum(int(item) for item in string))
    return int(string)


def sum_digits(n: int) -> int:
    """
    Суммирует цифры числа n.
    """
    return sum(int(d) for d in str(n))
