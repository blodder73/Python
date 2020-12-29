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
fruit['orange'] = "a sweet, orange citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, weet fruit growing in bunches"
fruit['lime'] = "a sour, greet citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])
fruit.close()

print(fruit)
