# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result = False
# print(id(result))
# print(id(another_result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))

result = "correct"
print(id(result))
