from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        col = defaultdict(set)
        raw = defaultdict(set)
        carre = defaultdict(set)

        for c in range(9):
            for r in range(9):

                value = board[c][r]

                if value == '.':
                    continue

                if (value in raw[c]
                    or value in col[r]
                    or value in carre[(c // 3, r // 3)]):
                    return False

                raw[c].add(value)
                col[r].add(value)
                carre[(c // 3, r // 3)].add(value)

        return True