class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2 == 1:
            return False
        dp = [[False for _ in range(sm//2 + 1)] for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(sm//2 + 1):
                if i == 0:
                    dp[i][j] = (j == nums[i] or j == 0)
                else:
                    dp[i][j] = dp[i-1][j] or (j-nums[i] >= 0 and dp[i-1][j-nums[i]])
        return dp[-1][-1]
                    