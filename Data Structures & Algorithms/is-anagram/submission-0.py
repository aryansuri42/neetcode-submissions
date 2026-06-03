class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counting(string):
            dicts = {}
            for i in string:
                if i in dicts.keys():
                    continue
                count = 0
                for j in string:
                    if i==j:
                        count+=1
                dicts[i] = count
            return dicts
        dicts = counting(s)
        dictt = counting(t)
        if dicts == dictt:
            return True
        return False