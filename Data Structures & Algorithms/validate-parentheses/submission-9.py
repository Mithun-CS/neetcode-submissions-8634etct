class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        bmap = {"}":"{",
        "]":"[",
        ")":"("
        }
        for i in s:
            if i in bmap:
                topelement = stack.pop() if stack else "#"
                if bmap[i] != topelement:
                    return False
            else:
                stack.append(i)
        return not stack
     

        
        