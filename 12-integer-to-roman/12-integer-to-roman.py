class Solution:
    def intToRoman(self, num: int) -> str:
        s = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        v = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        
        ans = ""
        for i in range(len(s)-1, -1, -1):
            while num >= v[i]:
                ans += s[i]
                num -= v[i]
        
        return ans