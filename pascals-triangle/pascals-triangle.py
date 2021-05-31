class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1], [1,1]]
        for i in range(1, numRows-1):
            ans.append(solve(ans[i]));
        return ans
        
def solve(row):
    return [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]