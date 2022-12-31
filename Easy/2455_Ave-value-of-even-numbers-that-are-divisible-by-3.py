# Given an integer array nums of positive integers, 
# return the average value of all even integers that are divisible by 3.
# Note that the average of n elements is the sum of the n elements divided by n 
# and rounded down to the nearest integer.

# Input: nums = [1,3,6,10,12,15]
# Output: 9
# Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.

# Input: nums = [1,2,4,7,10]
# Output: 0
# Explanation: There is no single number that satisfies the requirement, so return 0.

class Solution:
    def averageValue(self, nums: list[int]) -> int:
        count = 0
        sum = 0
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                sum += i
                count += 1
        if count == 0:  return 0
        return int(sum / count)