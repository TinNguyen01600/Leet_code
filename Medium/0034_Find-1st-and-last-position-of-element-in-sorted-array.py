# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        result = []
        if target not in nums:
            result.append(-1)
            result.append(-1)
        else:
            b = []
            for i in range(0, len(nums)):
                if nums[i] == target:  
                    b.append(i)
            result.append(b[0])
            result.append(b[-1])
        return result