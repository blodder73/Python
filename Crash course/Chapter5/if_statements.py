cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('\n')
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")

print('\n')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

print('\n')
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

print('\n')
age = 12
if age <= 4:
    print("Your admission cost is $0.")
elif age < 18 and age > 4:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40")

print('\n')
if age <= 4:
    price = 0
elif age < 18 and age > 4:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")