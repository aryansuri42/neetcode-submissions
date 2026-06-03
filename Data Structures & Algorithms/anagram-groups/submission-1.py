class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_chars = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in dict_chars:
                dict_chars[tuple(count)] = [s]
            else:
                dict_chars[tuple(count)].append(s)
        return list(dict_chars.values())
