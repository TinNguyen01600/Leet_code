# Given an array of integers arr, 
# return true if the number of occurrences of each value in the array is unique, or false otherwise.

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 
# 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# Input: arr = [1,2]
# Output: false

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occ = [0] * 2000    # array of 2000 0s 
        
        for i in arr:
            occ[i + 1000] += 1  # store the number of appearence of elements in (arr)
        new = [e for e in occ if e!=0]  # delete all 0s in (occ), store in (new)
        
        s = set()   # set cannot have mutable items
        for i in new:  s.add(i)     # select all distinct items from (new)

        # if len(s) == len(new) -> (new) contains all distinct numbers -> true   
        # else len(s) < len(new)
        return len(s) == len(new)