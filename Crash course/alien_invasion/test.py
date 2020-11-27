a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [4, 55, 1, 7, 1, 5, 10]
c = []

for number in a:
    if number in b:
        b.remove(number)
        print(b)