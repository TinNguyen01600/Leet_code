"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        max = 0
        while bool(nums):
            l = [e for e in nums if e == nums[0]]
            if len(l) > max: 
                max = len(l)
                result = l[0]
            nums = [e for e in nums if e != nums[0]]
        return result