class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # For rows
        for i in range(9):
            rows = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rows:
                        return False
                    else:
                        rows.add(board[i][j])

        # For columns
        for i in range(9):
            columns = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in columns:
                        return False
                    else:
                        columns.add(board[j][i])

        # For squares
        for s in range(9):
            square = set()
            for i in range(3):
                for j in range(3):
                    row = (s // 3) * 3 + i
                    column = (s % 3) * 3 + j
                    if board[row][column] != ".":
                        if board[row][column] in square:
                            return False
                        else:
                            square.add(board[row][column])
        return True