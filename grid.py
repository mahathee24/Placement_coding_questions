# Create M-shaped grid pattern using *
grid = [[" " for _ in range(10)] for _ in range(10)]

for i in range(10):
    for j in range(10):
        if j == 0 or j == 9:
            grid[i][j] = "*"
        if i == j and i < 5:
            grid[i][j] = "*"
        if i + j == 8 and i < 5:
            grid[i][j] = "*"

# Properly print the grid
for i in range(10):
    for j in range(10):
        print(grid[i][j], end=" ")
    print()  
