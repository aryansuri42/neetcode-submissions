class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = nums1 + nums2
        l1.sort()
        mid = len(l1)//2
        if len(l1)%2==0:
            median = (l1[mid] + l1[mid-1])/2
        else:
            median = l1[mid]
        return median