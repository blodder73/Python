sandwiches = ['tosti', 'tuna', 'salmon', 'gezond']
made_sandwich = []

while sandwiches:
    made = sandwiches.pop()

    print(f"Making {made.title()}")
    made_sandwich.append(made)

print(f"\nInhoud van sandwiches: ",sandwiches)
print(f"\nInhoud van made_sandwich: ", made_sandwich)