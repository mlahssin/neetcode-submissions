from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        col = defaultdict(list)
        raw = defaultdict(list)
        carre = defaultdict(list)

        for c in range(9):
            for r in range(9):

                if board[c][r] == ".":
                    continue
    
                if (board[c][r] in raw[c]
                    or board[c][r] in col[r] 
                    or board[c][r] in carre[(c//3, r//3)]):
                    return False
                raw[c].append(board[c][r])
                carre[(c//3, r//3)].append(board[c][r])
                col[r].append(board[c][r])
        return True