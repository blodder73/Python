menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

unwanted = "spam"
for meal in menu:
    while unwanted in meal:
        meal.remove("spam")
    print(meal)

print("\n\n")

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)

print("\n")

for meal in menu:
    for index, value in enumerate(reversed(meal)):
        if value == "spam":
            del value
    print(meal)

print("\n")

unwanted = "spam"
for meal in menu:
    if "spam" in meal:
        break

        for item in meal:
            print(item)
    else:
        print(meal)

print("\n")

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end = ", ")
    print()
