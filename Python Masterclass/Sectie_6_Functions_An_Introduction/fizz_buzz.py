def fizz_buzz (user_input: int) -> str:
    """
    When a `integer` is provided and the number is divisible by 3 then return `fizz`, whe divisible
    by 5 then return `buzz`. If divisible by 3 and 5, return `fizz_buzz`.
    :param user_input: whole numbers `int`
    """

    if (user_input % 3 == 0) and (user_input % 5 == 0):
        return "fizz buzz"
    elif user_input % 3 == 0:
        return "fizz"
    elif user_input % 5 == 0:
        return "buzz"
    else:
        return str(user_input)


for i in range(1, 101):
    print(fizz_buzz(i))