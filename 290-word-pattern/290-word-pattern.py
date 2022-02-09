class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ht = {}
        n = len(pattern)
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        for i in range(n):
            if pattern[i] in ht:
                if ht[pattern[i]] != words[i]:
                    return False
            ht[pattern[i]] = words[i]
            
        return len(set(pattern)) == len(set(words))