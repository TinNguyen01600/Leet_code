# Given an integer num, repeatedly add all its digits 
# until the result has only one digit, and return it.

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

# Input: num = 0
# Output: 0

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:    return num
        else:
            sum = 0
            while num != 0:
                sum += (num%10)
                num = int(num/10)
        return self.addDigits(sum)