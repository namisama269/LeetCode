class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [nums[-1]] * n
        
        for i in range(n-2, -1, -1):
            ans[i] = ans[i+1] * nums[i]
                
        prev = 1
        for i in range(n):
            if i > 0:
                prev *= nums[i-1]
            ans[i] = prev * (1 if i == n-1 else ans[i+1])
        
        return ans
    
    
    
    