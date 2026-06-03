class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isSafe(board, row, col, number):

            #Complete Row
            for i in range(len(board[0])):
                if board[row][i]==number and i!=col:
                    print(board[row][i])
                    print("row")
                    return False

            #Complete Col
            for i in range(len(board)):
                if board[i][col]==number and i!=row:
                    print("col")
                    return False

            #3x3Grid
            sqrt = int(math.sqrt(len(board)))
            rowStart = row - row%sqrt
            colStart = col - col%sqrt
            for i in range(rowStart, rowStart+sqrt):
                for j in range(colStart, colStart+sqrt):
                    if board[i][j]==number and i!=row and j!=col:
                        print("box")
                        return False
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!=".":
                    if isSafe(board, i, j, board[i][j]):
                        continue
                    else:
                        return False

        return True