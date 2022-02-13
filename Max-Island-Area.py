'''
Given a rectangular map with 0-1 entries,
find the maximal area of ones.
'''

def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
        return 0

    maxArea = 1
    grid[i][j] = '#'
    maxArea += dfs(grid, i+1, j)
    maxArea += dfs(grid, i-1, j)
    maxArea += dfs(grid, i, j+1)
    maxArea += dfs(grid, i, j-1)
    
    return maxArea


def maxIslandArea(grid):
    if not grid:
        return 0
    
    maxArea = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                maxArea = max(maxArea, dfs(grid, i, j))
    
    return maxArea

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxIslandArea(grid))