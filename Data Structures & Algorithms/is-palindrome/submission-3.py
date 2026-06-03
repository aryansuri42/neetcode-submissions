class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        s=s.lower()
        while start<len(s) and end>-1:
            if not s[start].isalnum():
                start+=1
            elif not s[end].isalnum():
                end-=1
            else:
                if s[start]==s[end]:
                    start+=1
                    end-=1
                else:
                    return False
        return True