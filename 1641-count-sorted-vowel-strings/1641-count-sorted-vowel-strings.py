class Solution:
    """
    dp[i][v] = number of str len i only vowels and lexicographically sorted
    ending in vowel v
    """
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 5 for _ in range(n)]
        
        for v in range(5):
            dp[0][v] = 1
            
        for i in range(1, n):
            for v in range(5):
                dp[i][v] = sum(dp[i-1][:v+1]) 
        
        return sum(dp[-1])