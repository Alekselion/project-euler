def ways(size):
    grid = [[0] * (size+1)] * (size+1)
    for c in range(size+1):
        grid[0][c] = 1
    for i in range(1, size+1):
        grid[i][0] = 1
        for j in range(1, size+1):
            grid[i][j] = grid[i][j-1] + grid[i-1][j]
    return grid[-1][-1]


task = "How many such routes are there through a 20×20 grid?"
result = ways(20)
print(f"Task: {task}\nAnswer: {result}")