from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def backtrack(r, c, i):
            if i == len(word):
                return True
                
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or
                (r, c) in path):
                return False
                
            path.add((r, c))
            
            res = (backtrack(r + 1, c, i + 1) or
                   backtrack(r - 1, c, i + 1) or
                   backtrack(r, c + 1, i + 1) or
                   backtrack(r, c - 1, i + 1))
                   
            path.remove((r, c))
            return res
            
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
                    
        return False