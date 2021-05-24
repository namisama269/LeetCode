class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)+1
        dp = [0] * (n)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + (0 if i == n-1 else cost[i])
        return dp[-1]
            
            