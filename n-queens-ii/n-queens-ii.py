class Solution:
    def totalNQueens(self, n: int) -> int:
        count = [0]
        col = [0 for _ in range(n)]
        diag1 = [0 for _ in range(1+2*(n-1))]
        diag2 = [0 for _ in range(1+2*(n-1))]
        search(count, col, diag1, diag2, n, 0)
        return count[0]

def search(count, col, diag1, diag2, n, y):
    if y == n:
        count[0] += 1
        return
    for x in range(n):
        if col[x] or diag1[x+y] or diag2[x-y+n-1]:
            continue
        col[x], diag1[x+y], diag2[x-y+n-1] = 1, 1, 1
        search(count, col, diag1, diag2, n, y+1)
        col[x], diag1[x+y], diag2[x-y+n-1] = 0, 0, 0