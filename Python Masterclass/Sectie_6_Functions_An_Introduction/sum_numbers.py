def sum_numbers(*args: float) -> float:
    """
    Accepts any number of input, ìnt` or `float` to add up
    :param arg: the provided numbers as `float`
    :return: the result as `float`
    """
    result = 0
    for i in args:
        result += i
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
