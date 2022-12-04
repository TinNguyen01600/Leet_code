#   Given two sorted arrays nums1 and nums2 of size m and n respectively, 
#   return the median of the two sorted arrays.

#   Input: nums1 = [1,3], nums2 = [2]
#   Output: 2.00000

#   Input: nums1 = [1,2], nums2 = [3,4]
#   Output: 2.50000

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a = []
        for i in nums1:
            a.append(i)
        for i in nums2:
            a.append(i)
        a.sort()
        pos = int(len(a)/2)
        if len(a) % 2 == 1:
            return float(a[pos])
        else:
            result = (a[pos] + a[pos-1]) / 2
            return result