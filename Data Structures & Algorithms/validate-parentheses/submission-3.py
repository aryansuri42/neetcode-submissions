class Solution:
    def isValid(self, s: str) -> bool:
        dp = {')':'(','}':'{',']':'['}
        stack = []
        def popping(index, s):
            if index>=len(s):
                if len(stack)>=1:
                    return False
                return True
            if s[index] not in dp:
                stack.append(s[index])
                return popping(index+1, s)
            if s[index] in dp:
                if len(stack)>=1 and stack[-1] == dp[s[index]]:
                    stack.pop()
                else:
                    stack.append(s[index])
                return popping(index+1, s)
        return popping(0, s)
            