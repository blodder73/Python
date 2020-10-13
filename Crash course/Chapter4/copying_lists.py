my_foods = ['pizza', 'falafel', 'carrot cake']

# this is not a copy but a new alias to my_foods
friend_foods = my_foods
print(friend_foods)
print(id(my_foods))
print(id(friend_foods))

# this is a true copy with new variable, check variable id
friend_foods = my_foods[:]
print(id(friend_foods))

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)
