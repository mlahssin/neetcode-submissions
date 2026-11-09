from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        raw = defaultdict(set)
        col = defaultdict(set)
        carre = defaultdict(set)

        for r in range(9):

            for c in range(9):

                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in raw[r] or board[r][c] in col[c]
                    or board[r][c] in carre[(r//3, c//3)]):
                    return False

                raw[r].add(board[r][c])
                col[c].add(board[r][c])
                carre[(r//3, c//3)].add(board[r][c])
        return True 


        