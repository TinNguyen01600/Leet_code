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
    def prime(self, n: int) -> bool:
        if n <= 1:  return False
        if n <= 3:  return True
        if n % 2 == 0 or n % 3 == 0:    return False
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i+2) == 0:    return False
            i += 6
        return True
    def isUgly(self, n: int) -> bool:
        if n == 1:  return True
        index = []
        for i in range(2, n+1):
            if not self.prime(i):    continue
            if n % i != 0:      continue
            index.append(i)
        for i in index:
            if i != 2 and i != 3 and i != 5:  return False
        return True