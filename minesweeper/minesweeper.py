class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if get_val(board, click) == 'M':
            set_val(board, click, 'X')
            return board
        return reveal(board, click)
        
deltas = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]        

def reveal(board, click):
    # Recursive reveal empty squares using flood fill/single square reveal
    if get_val(board, click) != 'E':
        return board
    n = count_adj(board, click)
    if n != 0:
        set_val(board, click, str(n))
    else:
        set_val(board, click, 'B')
        # Recursive reveal on adjacent squares
        for delta in deltas:
            adj = [click[0]+delta[0], click[1]+delta[1]]
            if on_board(board, adj):
                reveal(board, adj)
    return board

def count_adj(board, click):
    # Count how many mines are in at most 8 surrounding squares
    count = 0
    for delta in deltas:
        adj = [click[0]+delta[0], click[1]+delta[1]]
        if on_board(board, adj) and get_val(board, adj) == 'M':
            count += 1
    return count

def on_board(board, click):
    # Check if index is valid on the board
    r = len(board)
    c = len(board[0])
    return click[0] >= 0 and click[0] < r and click[1] >= 0 and click[1] < c

def get_val(board, click):
    # Get the value at a square on the board assuming within bounds
    return board[click[0]][click[1]]

def set_val(board, click, val):
    # Set the value at a square on the board assuming within bounds
    board[click[0]][click[1]] = val
    return board