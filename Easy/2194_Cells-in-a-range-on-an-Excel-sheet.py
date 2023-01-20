# Input: s = "K1:L2"
# Output: ["K1","K2","L1","L2"]
# Explanation:
# The above diagram shows the cells which should be present in the list.
# The red arrows denote the order in which the cells should be presented.

# Input: s = "A1:F1"
# Output: ["A1","B1","C1","D1","E1","F1"]
# Explanation:
# The above diagram shows the cells which should be present in the list.
# The red arrow denotes the order in which the cells should be presented.

class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        start_char = ord(s[0])
        end_char = ord(s[3])
        start_dig = int(s[1])
        end_dig = int(s[4])

        result = []
        for i in range(start_char, end_char + 1):
            for j in range(start_dig, end_dig + 1):
                temp = chr(i) + str(j)
                result.append(temp)
        return result