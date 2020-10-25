number = input("Write a number ")
number = int(number)

if number % 10 == 0:
    calc = number // 10
    print(f"Your {number} is a multiple of 10 by {calc} times")
else:
    print(f"Your {number} is not a multiple of 10")