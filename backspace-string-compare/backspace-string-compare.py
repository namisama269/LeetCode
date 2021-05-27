class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return solve(s) == solve(t)
        
def solve(string):
    ls = []
    for ch in string:
        if ch == '#':
            if ls != []:
                ls.pop()
        else:
            ls.append(ch)
    return ''.join(ls)