class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]
        
        found = False
        for i in range(m):
            if nums1[i] == nums2[0]:
                found = True
            dp[i][0] = 1 if found else 0
        
        found = False
        for j in range(n):
            if nums1[0] == nums2[j]:
                found = True
            dp[0][j] = 1 if found else 0
        
        for i in range(1, m):
            for j in range(1, n):
                    dp[i][j] = max(
                        dp[i-1][j-1] + (1 if nums1[i] == nums2[j] else 0),
                        dp[i-1][j],
                        dp[i][j-1]
                    )

        return dp[m-1][n-1]