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


input("Play Fizz Buzz.    Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
    else:
        print("Well done, you reached {}".format(next_number))