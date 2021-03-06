class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            mins = []
            for coin in coins:
                if i-coin >= 0 and dp[i-coin] != -1:
                    mins.append(dp[i-coin])
            if mins != []:
                dp[i] = 1 + min(mins)
            
        return dp[amount]

