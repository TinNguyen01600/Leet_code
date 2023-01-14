"""
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index 
is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Input: nums = [1,2,3]
Output: -1

Input: nums = [2,1,-1]
Output: 0
"""

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        nums.append(0)
        sum1, sum2 = 0, sum(nums)-nums[0]
        for i in range(len(nums) - 1):
            if sum1 == sum2:    return i
            else:
                sum1 += nums[i]
                sum2 -= nums[i+1]
        return -1