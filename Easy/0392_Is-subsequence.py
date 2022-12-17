"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "axc", t = "ahbgdc"
Output: false

Input: s = "ab", t = "baab"
Output: true

Input: s = "ab", t = "baba"
Output: true
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pos = []
        for i in s:
            if i not in t:  return False
            else:
                pos += [e for e in range(len(t)) if t[e] == i]
        for i in range(len(pos) - 1):
            if pos[i] >= pos[i+1]:   return False
        return True