def multiply(x, y):
    result = x * y
    return result


print(multiply(10.5, 4))
print(multiply(6, 7))

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)