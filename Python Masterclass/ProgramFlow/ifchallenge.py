name = input('What is your name? ')
age = int(input('How old are you {}? '.format(name)))

if 18 <= age < 31:
    print("{}, {} is a good age to go on holiday, have fun".format(name, age))
else:
    print("sorry {} you need to study more or work harder".format(name))