class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [0 for _ in range(n)]
        diag1 = [0 for _ in range(1+2*(n-1))]
        diag2 = [0 for _ in range(1+2*(n-1))]
        curr = ['.' * n for _ in range(n)]
        solns = []
        search(solns, col, diag1, diag2, curr, n, 0)
        return solns

def search(solns, col, diag1, diag2, curr, n, y):
    if y == n:
        solns.append(curr.copy())
        return
    for x in range(n):
        if col[x] or diag1[x+y] or diag2[x-y+n-1]:
            continue
        col[x], diag1[x+y], diag2[x-y+n-1] = 1, 1, 1
        curr[y] = modify_str(curr[y], x, 'Q')
        search(solns, col, diag1, diag2, curr, n, y+1)
        col[x], diag1[x+y], diag2[x-y+n-1] = 0, 0, 0
        curr[y] = modify_str(curr[y], x, '.')
        
def modify_str(string, index, val):
    return string[:index] + val + string[index+1:]