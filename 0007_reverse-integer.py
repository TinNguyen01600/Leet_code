#   Given a signed 32-bit integer x, return x with its digits reversed. 
#   If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

#   Input: x = 123
#   Output: 321

#   Input: x = -123
#   Output: -321

#   Input: x = 120
#   Output: 21

#   Input: x = 1534236469
#   Output: 0

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        n = x
        if x<0: n = abs(n)
        while n != 0:
            result *= 10
            result += (n%10)
            n = int(n/10)
        if result < (-2) ** 31: return 0
        elif result > 2**31 + 1: return 0
        elif x < 0:   return -result
        else:       return result