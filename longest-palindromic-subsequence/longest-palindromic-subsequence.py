class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*len(s) for _ in range(len(s))]
        return solve(s, dp, 0, len(s)-1)
def solve(s, dp, i, j):
    if dp[i][j]:
        return dp[i][j]
    if i > j:
        return 0
    elif i == j:
        dp[i][j] = 1
    elif s[i] == s[j]:
        dp[i][j] = 2 + solve(s, dp, i+1, j-1)
    else: # s[i] != s[j]
        dp[i][j] = max(solve(s, dp, i+1, j), solve(s, dp, i, j-1))       
    return dp[i][j]