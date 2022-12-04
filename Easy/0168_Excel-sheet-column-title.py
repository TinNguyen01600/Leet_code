# Given an integer columnNumber, 
# return its corresponding column title as it appears in an Excel sheet.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
# AZ -> 52
# ...
# ZZ -> 702
# AAA -> 703

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        result = ''
        while n != 0:
            remainder = n % 26
            n = int(n/26)
            if remainder == 0: 
                n -= 1
                remainder = 26
            result += chr(remainder + 64)
        return result[::-1]