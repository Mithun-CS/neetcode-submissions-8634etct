class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        brackmap ={"}":"{",
                 "]":"[",
                  ")":"(" }
        for i in s :
            if i in brackmap:
                topelement = stack.pop() if stack else '#'
                if brackmap[i] != topelement:
                    return False
            else:
                stack.append(i)

        return not stack

        
        