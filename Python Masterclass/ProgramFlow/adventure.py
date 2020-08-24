for i in range(0, 21):
    if (i % 3 != 0) and (i % 5 != 0):
        print(i)



available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.lower() == "quit":
        print("Game over")
        break
else:
    print("aren't you glad you got out of there")