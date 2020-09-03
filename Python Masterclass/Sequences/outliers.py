# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]

# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191,]

# data = [1014, 1015, 1104, 1105, 1110, 1120, 1130, 1130, 1150,
#         1160, 1170, 1183, 1185, 1187, 1188, 1191, 1350, 1360]

data = []

# del data[0:2]
# print(data)
# del data[14:]
# print(data)

print("\n")

min_valid = 100
max_valid = 200

# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         print(value)
#         del data[index]
# print(data)

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop) # for debugging
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, - 1, - 1):
    if data[index] <= max_valid:
        start = index + 1
        break

print(start) # for debugging
del data[start:]
print(data)
