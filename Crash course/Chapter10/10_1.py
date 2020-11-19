file = 'python_things.txt'

with open(file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print()

with open(file) as file_object:
    lines = file_object.read()

print(lines)

print()

lines = []
with open(file) as file_object:
    lines.append(file_object.readlines())
print(lines)