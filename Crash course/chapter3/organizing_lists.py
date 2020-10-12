cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

print('\n')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:', cars)
print('Here is the temporary sorted list:', sorted(cars))
print('Here is the original list:', cars)

# reverse a list permanently
print('\n')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print('Reverse order of cars', cars)

# Length of list
print('\n')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('the length of cars =', len(cars))