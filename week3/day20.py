class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, value: int) -> None:
        self.stack.append(value)
        if (len(self.min_stack) == 0 or self.getMin() >= value):
            self.min_stack.append(value)

    def pop(self) -> None:
        if (len(self.min_stack) > 0 and self.getMin() == self.top()):
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack)-1]

