from random import choice

lottery_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')
my_ticket = ['b', 2, 5, 'c']
count = 0

is_true = False

while not is_true:
    new_ticket = []
    i = 0
    j = 3
    while i <= j:
        new_ticket.append(choice(lottery_list))
        i += 1

    print(f"{count}. {new_ticket}")

    if new_ticket == my_ticket:
        is_true = True
    count += 1

print(f"In {count} keer is my_ticket {my_ticket} gelijk aan new_tick {new_ticket}")

