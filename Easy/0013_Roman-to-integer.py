# Given a roman numeral, convert it to an integer.

# Input: s = "III"
# Output: 3

# Input: s = "LVIII"
# Output: 58

# Input: s = "MCMXCIV"
# Output: 1994

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        mapper = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        r = []
        for i in s:
            r.append(mapper[i])
        for i in range(len(r)):
            if i == len(r)-1: result += r[i]
            elif r[i] < r[i+1]:   result -= r[i]
            else: result += r[i]
        return result