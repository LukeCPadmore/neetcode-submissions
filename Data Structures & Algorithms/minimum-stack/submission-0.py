class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.current_min.append(min(self.current_min[-1],val) if self.current_min else val)
        
    def pop(self) -> None:
        self.current_min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min[-1]
