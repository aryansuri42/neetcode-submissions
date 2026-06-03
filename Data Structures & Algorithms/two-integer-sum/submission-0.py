class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictindex = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in dictindex:
                return [dictindex[complement], i]
            dictindex[num] = i