prompt = "What is your age? "

while True:
    age = input(prompt)

    check_age = int(age)
    if check_age == 0:
        break
    elif check_age < 3:
        print("ticket is free")
    elif 3 <= check_age <= 12:
        print("ticket is $10")
    elif check_age > 12:
        print("ticket is $15")