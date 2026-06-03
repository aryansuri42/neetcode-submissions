class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listcheck=[]
        for i in nums:
            if i in listcheck:
                return True
            listcheck.append(i)
        return False