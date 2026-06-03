class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        low = 0
        high = len(s)-1
        while low<len(s) and high > -1:
            if s[low].isalnum() is False:
                low+=1
            elif s[high].isalnum() is False:
                high=high-1
            else:
                if s[low] == s[high]:
                    low+=1
                    high-=1
                else:
                    return False
        return True