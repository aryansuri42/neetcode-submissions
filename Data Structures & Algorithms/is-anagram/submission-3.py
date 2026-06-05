class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dps = {}
        dpt = {}
        for i in s:
            if i in dps:
                dps[i]+=1
            else:
                dps[i]=1

        for k in t:
            if k in dpt:
                dpt[k]+=1
            else:
                dpt[k]=1
        
        return dps == dpt