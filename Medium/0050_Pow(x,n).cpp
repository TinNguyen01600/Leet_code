/*
    Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
    Input: x = 2.00000, n = 10
    Output: 1024.00000

    Input: x = 2.10000, n = 3
    Output: 9.26100

    Input: x = 2.00000, n = -2
    Output: 0.25000
*/
#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

class Solution {
public:
    double myPow(double x, int n) {
        float result = 1;
        // cout << abs(n);
        for (int i = 0; i<abs(n); i++)  result *= x;
        if (n < 0)  result = 1 / result;
        return result;
    }
};