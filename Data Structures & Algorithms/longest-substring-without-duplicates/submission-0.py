class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        removed = 0
        longest = 0
        for i in range(len(s)):
            while s[i] in hashset:
                hashset.remove(s[removed])
                removed+=1
            w = (i - removed) + 1
            longest = max(longest, w)
            hashset.add(s[i])
        return longest

        