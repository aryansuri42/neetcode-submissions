class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(0,len(numbers)):
            diff = target - numbers[i]
            if diff in hashset:
                return [hashset[diff], i+1]
            if numbers[i] not in hashset:
                hashset[numbers[i]] = i+1
