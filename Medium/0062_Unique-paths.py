#   There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
#   The robot can only move either down or right at any point in time.
#   Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

#   Input: m = 3, n = 2
#   Output: 3

#   Input: m = 3, n = 7
#   Output: 28

#   m = 3, n = 2: there are 3 ways (R, D, D); (D, D, R); (D, R, D)
#   m = 2, n = 3: there are 3 ways (D, R, R); (R, D, R); (R, R, D)
#   m = 2, n = 4: there are 4 ways (D, R, R, R); (R, D, R, R); (R, R, D, R); (R, R, R, D)
#   It can be seen that for 1 grid, there are (m-1) Ds and (n-1) Rs
#   The problem is how many ways to arrange them.
#   You have (m-1 + n-1) seats, arrange Ds and Rs to them.
#   This is not similar to arranging k people to n seats;
#   because all Ds are the same, so are Rs; but more like picking k from n people.

#   there are nCk ways (C for combination)
#   nCk = (n!)/(k!(n-k)!)
#   So in this case, we pick (n-1) from (m-1 + n-1)
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        k = n - 1
        n = m-1 + n-1
        a = math.factorial(n)
        b = math.factorial(k)
        c = math.factorial(n-k)
        result = a/(b*c)
        return int(result)