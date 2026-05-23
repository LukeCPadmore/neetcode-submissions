class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        OPEN = ['(','{','[']
        CLOSE = [')','}',']']
        for ch in s: 
            if ch in CLOSE and not stack: 
                return False
            if ch in OPEN:
                stack.append(ch)
            if ch in CLOSE and CLOSE.index(ch) != OPEN.index(stack.pop()):
                return False

        
        return not stack

