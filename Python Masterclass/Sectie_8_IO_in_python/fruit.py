import shelve

# with shelve.open('shelfTest') as fruit:
#     fruit['orange'] = "a sweet, orange citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, weet fruit growing in bunches"
#     fruit['lime'] = "a sour, greet citrus fruit"
#
#     print(fruit["lemon"])
#     print(fruit["grape"])
#
# print(fruit)

# with shelve.open('shelfTest') as fruit:
#     fruit = {'orange': "a sweet, orange citrus fruit",
#     'apple': "good for making cider",
#     'lemon': "a sour, yellow citrus fruit",
#     'grape': "a small, weet fruit growing in bunches",
#     'lime': "a sour, greet citrus fruit"}
#
#     print(fruit["lemon"])
#     print(fruit["grape"])
#
# print(fruit)

# with shelve.open('shelfTest') as fruit:
fruit = shelve.open('shelfTest')
# fruit['orange'] = "a sweet, orange citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, weet fruit growing in bunches"
# fruit['lime'] = "a sour, greet citrus fruit"

# for snack in fruit:
#     print()
#     print(snack + ": " + fruit[snack])
#
# print(fruit["lemon"])
# print(fruit["grape"])

# fruit["lime"] = "great with tequila"
# for snack in fruit:
#     print(snack + ": " + fruit[snack])
#
# while True:
#     shelf_key = input("Please enter a fruit: ")
#     if shelf_key == "quit":
#         break
#
#     description = fruit.get(shelf_key, "We don't have a " + shelf_key)
#     print(description)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

print()

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()
