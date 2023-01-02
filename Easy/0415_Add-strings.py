"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.

Input: num1 = "11", num2 = "123"
Output: "134"

Input: num1 = "456", num2 = "77"
Output: "533"

Input: num1 = "0", num2 = "0"
Output: "0"
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1): num1, num2 = num2, num1
        temp = '0' * (len(num1) - len(num2))
        num2 = temp + num2

        result = ''
        n = 0
        for i in range(len(num1)-1, -1, -1):
            temp = int(num1[i]) + int(num2[i]) + n
            if temp > 9:
                temp %= 10
                n = 1
            else:   n = 0
            result += str(temp)
        if n == 1:  result += str(n)
        return result[::-1]