#   Given two binary strings a and b, return their sum as a binary string.

#   Input: a = "11", b = "1"
#   Output: "100"

#   Input: a = "1010", b = "1011"
#   Output: "10101"

#   Input: a = "11", b = "1111"
#   Output: "10010"

class Solution:
    def reform(self, a: str, l: int) -> str:
        c = ''
        for i in range(0, l-len(a)):
            c += '0'
        for i in range(0, len(a)):
            c += a[i]
        return c
    
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        if len(a) > len(b):     # b -> c
            l = len(a)
            b = self.reform(b, l)
        else:   # a -> c  
            l = len(b)
            a = self.reform(a, l)
        n = 0
        for i in range(l-1, -1, -1):
            temp = int(a[i]) + int(b[i]) + n
            if temp == 0:
                n = 0
                result += '0'
            elif temp == 1:
                n = 0
                result += '1'
            elif temp == 2:
                n = 1
                result += '0'
            else:
                n = 1
                result += '1'
        if n == 1:  result += '1'
        return result[::-1]
        