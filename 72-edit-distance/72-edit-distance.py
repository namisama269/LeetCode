class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = min(
                        # replace end, solve the rest
                        (0 if word1[i-1] == word2[j-1] else 1) + dp[i-1][j-1], 
                        # remove at start
                        1 + dp[i-1][j],
                        # insert at end
                        dp[i][j-1] + 1
                    )
            
        return dp[m][n]