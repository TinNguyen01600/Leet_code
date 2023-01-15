"""
    Given an array nums of distinct integers, return all the possible permutations. 
    You can return the answer in any order.
    
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

    Input: nums = [1]
    Output: [[1]]
"""

from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        perm = permutations(nums)
        for i in perm:
            result.append(list(i))
        return result