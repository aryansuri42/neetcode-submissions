class Solution:
    def isValid(self, s: str) -> bool:
        hashset = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in s:
            if i not in hashset:
                stack.append(i)
            elif i in hashset:
                if len(stack)>=1 and stack[-1] == hashset[i]:
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack)>0:
            return False
        return True