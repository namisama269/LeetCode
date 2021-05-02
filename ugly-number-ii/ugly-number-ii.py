class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        x0, x1, x2 = 0, 0, 0
        nums = [1]
        i = 2
        while i <= n:
            num = min(nums[x0]*2, nums[x1]*3, nums[x2]*5)
            if nums[x0]*2 == num:
                x0 += 1
            if nums[x1]*3 == num:
                x1 += 1
            if nums[x2]*5 == num:
                x2 += 1
            nums.append(num)
            i += 1
        return nums[-1]