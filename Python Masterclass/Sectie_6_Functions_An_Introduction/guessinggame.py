import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("'{}' is not a valid entry, please try a number.".format(temp))


highest = 1000
answer = random.randint(1, highest)
# print(answer)

guess = 0
count = 1
print("Please guess number between 1 and {}: ".format(highest))
while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        print("You pressed 0  to quit")
        break

    if guess == answer:
        if count != 1:
            print("Well done! You guessed it in {} tries".format(count))
        else:
            print("Well done! You guessed it in {} try".format(count))
    else:
        if guess < answer:
            print("Please guess higher")
        else: # guess must be greater than answer
            print("Please guess lower")
    count += 1

