"""
You are given two strings s and t.
String t is generated by random shuffling string s and then add one more letter at a random position.
Return the letter that was added to t.

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Input: s = "", t = "y"
Output: "y"

Input: s = "a", t = "aa"
Output: "a"
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if i not in s:  return i
            s = s.replace(i, '', 1) # delete the existed char from string s