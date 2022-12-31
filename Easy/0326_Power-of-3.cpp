/*
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.

Input: n = 27
Output: true
Explanation: 27 = 3^3

Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.

Input: n = -1
Output: false
Explanation: There is no x where 3^x = (-1).
*/
#include <iostream>
#include <string.h>
#include <math.h>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0) return false;
        float k = log10(double(n)) / log10(double(3));
        int x = int(k);
        return bool(int(pow(3, x)) == n);
    }
};