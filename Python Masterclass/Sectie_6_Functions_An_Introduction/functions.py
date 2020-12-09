def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


answer = multiply(10.5, 4)
print(answer)
print()
print(multiply(10.5, 4))
print(multiply(6, 7))

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
