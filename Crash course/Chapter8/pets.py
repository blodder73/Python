def describe_pet(pet_name, animal_type='dog'):
    """"Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('rat', 'Bella')
describe_pet('cat', 'Murchik')
describe_pet(animal_type='cat', pet_name='Murchik')
describe_pet(pet_name='Murchik', animal_type='cat')
describe_pet(pet_name='Willie')
describe_pet('Henk')
