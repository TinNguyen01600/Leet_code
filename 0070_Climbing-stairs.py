import math

#   You are climbing a staircase. It takes n steps to reach the top.
#   Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#   Input: n = 2
#   Output: 2
#   Explanation: There are two ways to climb to the top.
#   1. 1 step + 1 step
#   2. 2 steps

#   Input: n = 3
#   Output: 3

#   n = 4, output = 5
#   1. 1 1 1 1 -> 4C0
#
#   2. 1 1 2  
#   3. 1 2 1   -> 3C1
#   4. 2 1 1  
#
#   5. 2 2     -> 2C2

#   n = 5, output = 8
#   1. 1 1 1 1 1 -> 5C0
#
#   2. 2 1 1 1
#   3. 1 2 1 1
#   4. 1 1 2 1   -> 4C1
#   5. 1 1 1 2
# 
#   6. 1 2 2
#   7. 2 1 2     -> 3C2
#   8. 2 2 1

class Solution:
    def combination(self, n: int, k: int) -> int:
        a = math.factorial(n)
        b = math.factorial(n-k)
        c = math.factorial(k)
        return int(a/(b*c))
    def climbStairs(self, n: int) -> int:
        k = 0
        sum = 0
        while n>=k:
            sum += self.combination(n, k)
            n -= 1
            k += 1
        return sum