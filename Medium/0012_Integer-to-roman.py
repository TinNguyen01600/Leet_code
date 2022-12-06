# Given an integer, convert it to a roman numeral.

# Input: num = 3
# Output: "III"

# Input: num = 58
# Output: "LVIII"

# Input: num = 1994
# Output: "MCMXCIV"

# I divide the number into many parts in decimal, then convert each part
# For ex, num = 1234 -> digit = [4,3,2,1] = 4 + 30 + 200 + 1000
# I put it in for loop and convert temp = digit[i]*(10**i) to roman

class Solution:
    def check_special(self, num: int, integer: list, roman: list) -> str:
        result = ''
        pos = [j for j in range(len(integer)) if integer[j] == num]
        if bool(pos):   result += roman[pos[0]]
        return result
    
    def intToRoman(self, num: int) -> str:
        integer = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        result = ''
        digit = []
        while num != 0:
            digit.append(num % 10)
            num = int(num/10)

        i = len(digit)
        temp = 0
        while i >= 0:
            if temp != 0:
                special = self.check_special(temp, integer, roman)
                if bool(special):     result += special     # check if temp in [special_int]  
                else:
                    pos = [j for j in range(len(integer)) if integer[j] < temp][-1]
                    division = int(temp / integer[pos])
                    remainder = temp % integer[pos]
                    for k in range(division):   result += roman[pos]
                    temp = remainder
                    continue
            i -= 1
            temp = digit[i] * (10**i)
        return result