"""
Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        occ = [0] * 75
        for i in s:
            occ[ord(i) - 48] += 1
        new_occ = [e for e in occ if e!=0]

        even = [e for e in new_occ if e%2==0]
        odd = [e for e in new_occ if e%2!=0]

        result = 0
        if bool(even):   result += sum(even)
        if bool(odd):   result += (sum(odd) - (len(odd) - 1))
        return result