# import random
#
# highest = 10
# answer = random.randint(1, highest)
# print(answer)   # TODO: Remove after testing
#
# print("Please guess number between 1 and {}: ".format(highest))
# guess = int(input())
#
# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else: # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")

import random

highest = 1000
answer = random.randint(1, highest)
# print(answer)

guess = 0
count = 1
print("Please guess number between 1 and {}: ".format(highest))
while guess != answer:
    guess = int(input())
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

