"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
"""

class Solution:
    def letterCombinations(self, s: str) -> list[str]:
        result = []
        if not bool(s):    return result
        num2letters = []
        ascii = 97
        for i in range(8):
            temp = []
            if i == 5 or i == 7:  letter = 4
            else:   letter = 3 
            for j in range(letter):
                temp.append(chr(ascii + j))
            num2letters.append(temp)
            ascii += letter
        
        for i in num2letters[int(s[0]) - 2]:
            if len(s) > 1:
                for j in num2letters[int(s[1]) - 2]:
                    if len(s) > 2:
                        for k in num2letters[int(s[2]) - 2]:
                            if len(s) > 3:
                                for l in num2letters[int(s[3]) - 2]:
                                    result.append(i + j + k + l)
                            else:   result.append(i + j + k)
                    else:   result.append(i + j)
            else:   result.append(i)
        return result