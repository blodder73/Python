def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()

def palindrome_sentence(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += char
    # return result[::-1].casefold() == result.casefold()
    return is_palindrome(result)


word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))


# is_palindrome("Was it a car, or a cat, I saw?")
# is_palindrome("Can't you see 4 sure?")
# is_palindrome("Do geese see god?")
# is_palindrome("Desnes not far, Rafton sensed")