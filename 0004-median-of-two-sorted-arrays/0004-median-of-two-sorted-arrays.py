class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = sorted(nums1 + nums2)
        if len(merge) % 2:
            return float(merge[len(merge)//2])
        else:
            return (merge[(len(merge)//2)-1] + merge[len(merge)//2]) / 2