for i in range(10, 16):
    print("i is now {}".format(i))


for i in range(0, 11, 2):
    print(i)

for i in range(10, -1, -2):
    print(i)


age = int(input("How old are you? "))

if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

for i in range(0, 101):
    if i % 7 == 0:
        print(i)
