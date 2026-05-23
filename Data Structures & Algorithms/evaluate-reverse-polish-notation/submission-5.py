class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPS = {'+':int.__add__, '-':int.__sub__, '*':int.__mul__,'/':lambda a, b: int(a / b)}
        for t in tokens: 
            if t not in OPS:
                stack.append(int(t))
            else:
                t2,t1 = stack.pop(),stack.pop()
                stack.append(OPS[t](t1,t2))


        return stack.pop()