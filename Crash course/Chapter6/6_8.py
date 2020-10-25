Pets = []

cats = {
    'Murchick': {
        'eigenaar': 'Elmira',
        'leeftijd': '11 jaar',
    },

    'Pusha': {
        'eigenaar': 'Buddy',
        'leeftijd': '11 jaar',
    },
}

rats = {
    'Bella': {
        'eigenaar': 'Mira',
        'leeftijd': '12 weken',
    },

    'Feyenna': {
        'eigenaar': 'Feyenna',
        'leeftijd': '9 weken'
    }
}

Pets = [cats, rats]

for pet in Pets:
    for naam, dier_info in pet.items():
        print(naam.title(), '\t', dier_info['eigenaar'], ' ', dier_info['leeftijd'])