'''
Given a grid with obstacles (ones). Calculate the number of paths.
'''

def uniquePathsWithObstacles(grid):
    if grid[-1][-1] == 1 or grid[0][0] == 1 or not grid:
        return 0

    dp = [[0] * len(grid[0]) for i in range(len(grid))]
    dp[0][0] = 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                dp[i][j] += dp[i-1][j] if i >= 1 else 0
                dp[i][j] += dp[i][j-1] if j >= 1 else 0

    return dp[-1][-1]

print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))