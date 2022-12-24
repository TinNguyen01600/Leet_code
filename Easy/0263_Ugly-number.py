"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Input: n = 6
Output: true
Explanation: 6 = 2 x 3

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
"""

class Solution:
    def decrease(self, n: int) -> int:
        if n % 2 == 0:  n /= 2
        elif n % 3 == 0:    n /= 3
        elif n % 5 == 0:    n /= 5
        else:   return n
        return self.decrease(n)
    def isUgly(self, n: int) -> bool:
        if n == 1:  return True
        if n <= 0:   return False
        if int(self.decrease(n)) == 1:   return True
        return False