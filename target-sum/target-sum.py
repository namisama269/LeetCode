class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        mins = (-1)*total
        if target < mins or target > total:
            return 0
        dp = [([0]*(1+2*total)) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(1+2*total):
                if i == 0:
                    if (j+mins) == nums[i]:
                        dp[i][j] += 1
                    if (j+mins) == (-1)*nums[i]:
                        dp[i][j] += 1
                else:
                    if j-nums[i] >= 0:
                        dp[i][j] += dp[i-1][j-nums[i]]
                    if j+nums[i] <= 2*total:
                        dp[i][j] += dp[i-1][j+nums[i]]
        return dp[len(nums)-1][total+target]