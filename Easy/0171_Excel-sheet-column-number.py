# Given a string columnTitle that represents the column title 
# as appears in an Excel sheet, return its corresponding column number.

# Input: columnTitle = "A"
# Output: 1

# Input: columnTitle = "AB"
# Output: 28

# Input: columnTitle = "ZY"
# Output: 701

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        a = []
        for i in columnTitle:
            a.append(ord(i)-64) 
        result = 0
        for i in range(0, len(a)):
            result = result * 26 + a[i]
        return result