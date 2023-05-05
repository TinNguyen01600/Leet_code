/*
You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Input: n = 8
Output: 3

1 <= n <= 2^31 - 1
*/

/*
1 row : 1 coin
2 rows : 3 coins
3 rows : 6 coins
...
x rows : x(x+1)/2 coins -- (sum from 1 to x)

We have n coins -> find x
x(x+1)/2 = n
<=> x^2 + x = 2n <=> (x+1/2)^2 = 2n + 1/4
<=> x = sqrt(2n + 1/4) - 1/2 (we only get positive root)
*/

#include <math.h>

class Solution {
public:
    int arrangeCoins(int n) {
        double num = n;     // extend the size of n because we have 2n
        // range 2^31 -> 2^32
        return (int)(sqrt(2*num + 0.25) - 0.5);
    }
};