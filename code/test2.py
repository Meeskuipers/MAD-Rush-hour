width = int(input("How wide?"))
height = int(input("How high?"))
grid = []
row = []
bak = "."
for i in range(width):
    row.append('car')
for i in range(height):
    grid.append(row)
for i in range(len(grid)):
    print(grid[i])
