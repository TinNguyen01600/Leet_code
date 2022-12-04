#   Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#   You must not use any built-in exponent function or operator.
#   For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

#   Input: x = 4
#   Output: 2

#   Input: x = 8
#   Output: 2

#   Input: x = 6
#   Output: 2

#   Input: x = 0
#   Output: 0

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:  return 0
        half = int(x/2)
        i = 1
        while i<half:
            i += 1
            if i*i > x: return i-1
        return i