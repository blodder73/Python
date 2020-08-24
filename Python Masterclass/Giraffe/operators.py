a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

print()

for i in range(1, 4):
    print(i)

for i in range(1, a // b):
    print(i)

print(a + b // 3 - 4 * 12 ) #12 + 1 - 48 = -35

nums = [1,2,3,4,5,6,7,8,9,10]
result = [x*x for x in nums if x % 2 == 0]
print(result)

#Operator Precedence Acronyms
#PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

print()
print(a / (b * a) / b) # 12 / (3 * 12) / 3 = 12 / 36 /3 = 1 / 3 / 3= 0,333333 / 3 = 0,11111