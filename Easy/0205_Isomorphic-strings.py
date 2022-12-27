"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_char, t_char = [],[]
        for i in range(len(s)):
            if s[i] not in s_char: s_char.append(s[i])
            if t[i] not in t_char: t_char.append(t[i])

        if len(s_char) != len(t_char):  return False

        s_pos, t_pos = [], []
        for i in range(len(s_char)):
            temp1 = [e for e in range(len(s)) if s[e] == s_char[i]]
            s_pos.append(temp1)
            temp2 = [e for e in range(len(t)) if t[e] == t_char[i]]
            t_pos.append(temp2)
        for i in range(len(s_pos)):
            if s_pos[i] != t_pos[i]:    return False
        return True