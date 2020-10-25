favorite_places = {
    'Elmira': {
        '1': 'Oekraine',
        '2': 'Oostenrijk',
        '3': 'Nederland',
    },

    'Mira': {
        '1': 'Plaswijckpark',
        '2': 'Efteling',
        '3': 'in de wijk',
    },

    'Buddy': {
        '1': 'Thuis',
        '2': 'Oostenrijk',
        '3': 'Centerparc',
    },
}

for naam, info in favorite_places.items():
    print(f"{naam.title()}")
    for item, place in info.items():
        print(f"\t{item} : {place.title()}")
    print()