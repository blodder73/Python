number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [0]
]

print(number_grid[1][2])

for row in number_grid:
    for column in number_grid:
        print(str(row) + " , " + str(column))