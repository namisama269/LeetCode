class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    # Check if can increase the square at this location
                    prev = dp[i-1][j-1]
                    steps = 0
                    for k in range(1, prev+1):
                        if matrix[i-k][j] == '1' and matrix[i][j-k] == '1':
                            steps += 1
                        else:
                            break
                    dp[i][j] = 1 + steps
        
        return max(map(max,dp))**2