words = {
    'get': 'get item from dictonary, empty results not in an error',
    'for': 'to make a loop through a list',
    'print': 'print output to screen',
    'del': 'delete item from list or dictonary',
    'set': 'makes a set, only unique values will be displayed',
    'sort': 'sort values',
}

print(f"get: {words['get']}")
print(f"for: {words['for']}")
print(f"print: {words['print']}")
print(f"del: {words['del']}")

print("\n")
for k, v in words.items():
    print(f"{k.title()}: {v.title()}")
