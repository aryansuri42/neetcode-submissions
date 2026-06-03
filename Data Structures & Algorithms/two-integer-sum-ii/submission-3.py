class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start<end:
            currsum = numbers[start] + numbers[end]

            if currsum>target:
                end-=1
            elif currsum<target:
                start+=1
            else:
                return [start+1, end+1]
        return []