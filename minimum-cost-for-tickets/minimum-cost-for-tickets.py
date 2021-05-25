class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(days[-1]+1)]
        curr = 0
        
        for i in range(1, len(dp)):
            if i < days[curr]:
                dp[i] = dp[i-1]
            else:
                c1 = dp[i-1] + costs[0]
                c7 = dp[max(0, i-7)] + costs[1]
                c30 = dp[max(0, i-30)] + costs[2]
                dp[i] = min(c1,c7,c30)
                curr += 1
        
        return dp[-1]