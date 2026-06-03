class MinStack:

    def __init__(self):
        self.output_stack = ["MinStack"]
        self.stack = []

    def push(self, val: int) -> None:
        self.output_stack.append("null")
        self.stack.append(val)
        return

    def pop(self) -> None:
        popped = self.stack.pop()
        self.output_stack.append(popped)
        return

    def top(self) -> int:
        top = self.stack[-1]
        self.output_stack.append(top)
        return top

    def getMin(self) -> int:
        minimum = min(self.stack)
        self.output_stack.append(minimum)
        return minimum
        
