#value = 10 / 0

try:
    #value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Divide by zero error")
    print(err)
except ValueError as verr:
    print("You didn't enter a number!")
    print(verr)