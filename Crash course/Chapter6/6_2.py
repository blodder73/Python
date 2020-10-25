#favorite_numbers = {'Elmira': '7', 'Buddy': '11', 'Mira': '10'}

favorite_numbers = {'Elmira': ['7'], 'Buddy': ['7','11'], 'Mira': ['3', '7', '10']}


print(favorite_numbers)

for naam, items in favorite_numbers.items():
    print(f"{naam.title()}")
    for nummer in items:
        print(nummer)
    print()