def factorial(get_number: int) -> int:
    """
    Does a factorial calculation
    :param get_number: the integer from counting
    :return: the factorial integer
    """
    fact = 1
    for i in range(1, get_number + 1):
        fact = fact * i
    return str(fact)


for j in range(0, 36):
    print(j, factorial(j))