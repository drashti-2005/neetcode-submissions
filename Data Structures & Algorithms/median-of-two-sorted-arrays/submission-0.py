class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        n = len(nums1)

        if n % 2 == 0:
            m1 = n // 2 - 1
            m2 = n // 2
            return (nums1[m1] + nums1[m2]) / 2
        else:
            return nums1[n // 2]