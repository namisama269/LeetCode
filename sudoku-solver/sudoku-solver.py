class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solve(board)
       
            
def solve(board):
    x, y = get_next(board)
    if x is None:
        return True

    for i in range(1,10):
        if is_valid(board, x, y, str(i)):
            board[x][y] = str(i)
            if solve(board):
                return True
        board[x][y] = '.'
        
    return False
        
def get_next(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return i,j
    return None,None   
        
def is_valid(board, i, j, num):
    # row
    if num in board[i]:
        return False
    # col
    if num in [board[x][j] for x in range(9)]:
        return False
    # square
    sq = []
    for x in range(i-i%3, i-i%3+3):
        for y in range(j-j%3, j-j%3+3):
            sq.append(board[x][y])
    if num in sq:
        return False
    return True