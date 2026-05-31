class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Scan each row, checking that each row has unique vals
        row_seen = set()
        for i in range(len(board)): 
            for j in range(len(board)):
                if board[i][j] in row_seen:
                    return False
                else:
                    if board[i][j] != '.':
                        row_seen.add(board[i][j])
            row_seen = set()

        # Same as above, but with columns
        col_seen = set()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] in col_seen:
                    return False
                else:
                    if board[j][i] != '.':
                        col_seen.add(board[j][i])
            col_seen = set()

        square_seen = set()
        # We have 9 boxes, each row and column has a start index of 0, 3, or 6
        # Technically this is O(81)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                    for k in range(3):
                        for l in range(3):
                            if board[i + k][j + l] in square_seen:
                                return False
                            else:
                                if board[i + k][j + l] != '.':
                                    square_seen.add(board[i + k][j + l])
                    square_seen = set()

        return True

            

        

        


            