import json

filename = 'favorite_number.json'

with open(filename, 'w') as f:
    number = input("what is your favorite number? ")
    json.dump(number, f)