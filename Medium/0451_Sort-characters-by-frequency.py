# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. 
# If there are multiple answers, return any of them.

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

# Input: s = "2a554442f544asfasssffffasss"
# Output: "sssssssffffff44444aaaa55522"

class Solution:
    def frequencySort(self, s: str) -> str:
        occ = [0] * 75
        for i in s:
            occ[ord(i) - 48] += 1
        distinct_char = []
        for i in range(0, len(occ)):
            if occ[i] != 0: distinct_char.append(chr(i+48))
        new_occ = [e for e in occ if e!=0]
        
        for i in range(0, len(new_occ)):
            for j in range(i+1, len(new_occ)):
                if new_occ[i] < new_occ[j]:
                    temp = new_occ[i]
                    new_occ[i] = new_occ[j]
                    new_occ[j] = temp

                    temp = distinct_char[i]
                    distinct_char[i] = distinct_char[j]
                    distinct_char[j] = temp
        result = ''
        for i in range(0, len(new_occ)):
            for j in range(0, new_occ[i]):   result += distinct_char[i]
        return result