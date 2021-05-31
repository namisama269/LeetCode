class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        ans = [1,1]
        for i in range(rowIndex-1):
            ans = solve(ans)
        return ans
        
def solve(row):
    return [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]