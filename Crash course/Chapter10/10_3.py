file = 'guest.txt'

with open(file, 'a') as file_object:
    ask = input("What is your name? ")
    file_object.write(ask + '\n')