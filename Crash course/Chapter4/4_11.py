pizzas = ['margharita', 'salami', 'hawai']
for pizza in pizzas:
    print(pizza)

print("\nI love pizza\n")

friend_pizzas = pizzas[:]
pizzas.append('onion')
friend_pizzas.append('meatloaf')
print('my pizza\'s', pizzas, ' , id = ', id(pizzas))
print('friends pizza\'s', friend_pizzas, ' , id = ', id(friend_pizzas))

for food in pizzas:
    print(food)