from random import randint


def roll_die(die=6):
    print(f"{randint(1,die)}")


roll_die()

print("10 x D6")
for i in range(1, 10):
    roll_die()

print("10 x D10")
for i in range(1, 10):
    roll_die(10)

print("10 x D20")
for i in range(1, 10):
    roll_die(20)