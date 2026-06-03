class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def create_dict(dictn, string):
            for i in range(len(string)):
                if string[i] not in dictn:
                    dictn[string[i]] = 1
                else:
                    dictn[string[i]] += 1
            return dictn
        dict1 = create_dict({},s)
        dict2 = create_dict({},t)
        if dict1==dict2:
            return True
        return False
                   