file = 'guest_book.txt'
with open(file, 'a') as file_object:
    while True:
        print("(enter 'q' at any time to quit)")
        ask = input("What is your name? ")
        if ask.lower() != 'q':
            print(f"Hello {ask.title()}!")
            file_object.write(ask + '\n')
        else:
            break
