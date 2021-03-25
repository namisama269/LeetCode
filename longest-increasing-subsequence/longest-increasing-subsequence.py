class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = n * [1]
        prev = n * [-1]
        for i in range(1, n):
            curr_max = 0
            curr_idx = -1
            for j in range(i):
                if nums[j] < nums[i] and dp[j] > curr_max:
                    curr_max = dp[j]
                    curr_idx = j
            dp[i] = 1 + curr_max
            prev[i] = curr_idx
        # Backtrack from prev to get the subsequence
        ans = []
        # Get the max len(LIS) and index of last element
        max_len = 1
        max_idx = -1
        for idx, lis_len in enumerate(dp):
            if lis_len > max_len:
                max_len = lis_len
                max_idx = idx
        k = max_idx
        while prev[k] != -1:
            ans.append(nums[k])
            k = prev[k]
        ans.append(nums[k]) # add the first element of LIS
        ans.reverse()
        return max_len