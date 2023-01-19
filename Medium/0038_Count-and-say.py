"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that 
each substring contains exactly one unique digit. Then for each substring, say the number of digits, 
then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251" is "23321511"

n = 1: return 1 is the base case
n = 2: return count of last entry i.e. 1 1
n = 3: return count of last entry i.e. two 1's so 21
n = 4: we have one 2 and one 1 so 1211
n = 5: , we have one 1 and one 2 and two 1's so -> 111221
n = 6: we have three 1's, two 2's and one 1 so -> 312211
n = 7: we have one 3, one 1, two 2's and two 1's -> 13112221
"""

class Solution:
    def say(self, s: str):
        if s == '1':    return '11'
        
        result = ''
        count = 0; temp = s[0]
        for i in range(len(s)):
            if s[i] != temp:
                result += (str(count) + s[i-1])
                temp = s[i]
                count = 1
            else:
                count += 1
        result += (str(count) + s[-1])
        return result
    def countAndSay(self, n: int) -> str:
        temp = '1'
        for i in range(n-1):
            temp = self.say(temp)
        return temp
        