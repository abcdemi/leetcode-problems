'''
Given a rectangular map with 0-1 entries,
find the number of contiguous ones.
'''

def dfs(grid, i, j):
    grid[i][j] = 0
    for h, v in (1,0), (-1,0), (0,-1), (0,1):
        horizontal = i + h
        vertical = j + v
        if 0 <= horizontal < len(grid) and \
            0 <= vertical < len(grid[0]) and grid[horizontal][vertical] == 1:
            dfs(grid, horizontal, vertical)

def numIslands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(grid, i, j)
                count += 1
    return count

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(numIslands(grid))