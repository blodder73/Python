empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even , odd]
print(numbers)
print("\n")

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
# print(len(even))
# print(len(odd))
#
# print()
# print("mississippi".count("issi"))
#
# even.extend(odd)
# print(even)
#
# even.sort()
# print(even)
#
# another_even = even
# print(another_even)
#
# even.sort(reverse=True)
# print(even)
# print(another_even)
#
# print("\n")
# empty_list = []
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# print(numbers)
#
# sorted_numbers = list(numbers)
# print(sorted_numbers)
# print(numbers)
#
# digits = sorted("432985617")
# print(digits)
#
# print("\n")
#
# #more_numbers = list(numbers)
# #more_numbers = numbers[:]
# more_numbers = numbers.copy()
# print(more_numbers)
#
# print(numbers is more_numbers)
# print(numbers == more_numbers)
