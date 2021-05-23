class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = 1 + min([dp[i-sq] for sq in squares if i-sq >= 0])
        return dp[-1]
                