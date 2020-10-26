sandwiches = ['pastrami', 'tosti', 'pastrami', 'tuna', 'pastrami', 'salmon', 'pastrami', 'gezond']
print("The Deli has run out of Pastrami")

print(sandwiches)

while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')

print(sandwiches)

made_sandwich = []

while sandwiches:
    made = sandwiches.pop()

    print(f"Making {made.title()}")
    made_sandwich.append(made)

print(f"\nInhoud van sandwiches: ",sandwiches)
print(f"\nInhoud van made_sandwich: ", made_sandwich)