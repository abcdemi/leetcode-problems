def maximalSquare(matrix):
    m, n = len(matrix), len(matrix[0])
    result = 0
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j] if i > 0 else 0, \
                    dp[j-1][i] if j > 0 else 0,\
                        dp[i-1][j-1] if i > 0 and j > 0 else 0) + 1
                if dp[i][j] > result:
                    result = dp[i][j]
    return result * result

A = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(A))