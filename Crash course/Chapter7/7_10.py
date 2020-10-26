response = {}
polling = True

while polling:
    name = input("Wat is je naam? ")
    location = input("Waar wil je op vakantie? ")
    response[name] = location

    repeat = input("Nog meer mensen die op vakntie willen? (ja/nee) \n")
    if repeat == 'nee':
        polling = False

print()
for name, location in response.items():
    print(f"{name.title()}, wil graag naar {location.title()}")
print(response)