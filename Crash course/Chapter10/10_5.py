file = "like_python.txt"

with open(file, 'a') as file_object:
    while True:
        ask = input("Why you like programming? ")
        if ask.lower() != 'q':
            file_object.write(ask + '\n')
        else:
            break