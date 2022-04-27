class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows + cols
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j] in row or board[j][i] in col:
                    return False
                if board[i][j] != '.':
                    row.add(board[i][j])
                if board[j][i] != '.':
                    col.add(board[j][i])

        # 3x3 squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sqr = set()
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] in sqr:
                            return False
                        if board[i+x][j+y] != '.':
                            sqr.add(board[i+x][j+y])

        return True