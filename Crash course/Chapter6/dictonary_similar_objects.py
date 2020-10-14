favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['phil'].title()
print(f"Sarah's favorite language is {language}.")

print("\n")
alien_0 = { 'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])  --- dit geeft een error get() niet
point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

print("\n")
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")
for value in favorite_languages.values():
    print(value.title())

print("\n")
for name in favorite_languages:
    print(name.title())

print("\n")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        #language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {favorite_languages[name].title()}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")