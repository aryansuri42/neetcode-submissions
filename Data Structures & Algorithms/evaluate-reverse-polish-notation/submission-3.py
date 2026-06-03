class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i=="+":
                    ans = b+a
                elif i=="-":
                    ans = b-a
                elif i=="*":
                    ans = b*a
                elif i=="/":
                    ans = int(b/a)
                stack.append(ans)
        return stack[0]
