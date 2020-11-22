import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    with open(filename, 'w') as f:
        number = input("what is your favorite number? ")
        json.dump(number, f)
else:
    print(f"Your favorite number is {number}!")




