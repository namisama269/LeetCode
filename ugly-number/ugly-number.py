class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return is_subset(set(factors(n)), [2,3,5])
    
def factors(n):
    ans = []
    i = 2
    while i <= math.sqrt(n):
        while n % i == 0:
            n //= i
            ans.append(i)
        i = 3 if i == 2 else i + 2
    if n != 1:
        ans.append(int(n))
    return ans

def is_subset(a, b):
    for elem in a:
        if elem not in b:
            return False
    return True