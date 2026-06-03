class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i not in res.keys():
                res[i]=1
                continue
            res[i]+=1
        for n, c in res.items():
            freq[c].append(n)
        
        res_out = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res_out.append(n)
                if len(res_out) == k:
                    return res_out
            