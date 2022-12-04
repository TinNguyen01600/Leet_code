/*
    Given two positive integers a and b, return the number of common factors of a and b.
    An integer x is a common factor of a and b if x divides both a and b.

    Input: a = 12, b = 6
    Output: 4
    Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

    Input: a = 25, b = 30
    Output: 2
    Explanation: The common factors of 25 and 30 are 1, 5.
*/
#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

class Solution {
public:
    int commonFactors(int a, int b) {
        int small = (a < b) ? a : b;
        int result = 0;
        for (int i = 1; i<=small; i++){
            if ((a % i == 0) && (b % i == 0))   result++;
        }
        return result;
    }
};