"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Input: nums1 = [3,1,2], nums2 = [1,1]
Output: [1]
"""

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        result = []
        for i in nums1:
            if i in nums2:  
                nums2.remove(i)
                result.append(i)
        return result