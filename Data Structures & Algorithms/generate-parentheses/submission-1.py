from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open_p, close_p, current):
            if open_p == close_p == n:
                res.append(current)
                return
            
            if open_p < n:
                backtrack(open_p + 1, close_p, current + "(")
                
            if close_p < open_p:
                backtrack(open_p, close_p + 1, current + ")")
                
        backtrack(0, 0, "")
        return res