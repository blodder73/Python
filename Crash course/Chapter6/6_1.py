persons = []

wife = {'naam': 'Elmira', 'geslacht': 'vrouw', 'land': "Oekraine", 'kinderen': '2'}
# print(wife['naam'])
# print(wife['geslacht'])
# print(wife['land'])
# print(wife['kinderen'])

colleague = {
    'Bob': 'Den Haag',
    'Ali': 'Den Haag',
    'Jorg': 'Delft',
}

familie = {
    'Ellen': 'Dronten',
    'ma': 'Rotterdam',
    'Ryuken': 'Rotterdam',
}
persons = [wife, colleague, familie]

for person in persons:
    for naam, woonplaats in person.items():
        print(naam, ' ', woonplaats)

    print("\n")