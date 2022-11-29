# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Input: n = 1
# Output: true

# Input: n = 3
# Output: false

import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:   return False
        x = int(math.log2(n))
        if 2**x == n:   return True
        else:   return False