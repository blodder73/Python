for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)
uneven_numbers = list(range(1, 11, 2))
print(uneven_numbers)
print("\n")

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

print("\n")
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

print("\n")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print("\n")
squares = [value**2 for value in range(1, 11)]
print(squares)