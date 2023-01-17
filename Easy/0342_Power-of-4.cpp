/*
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4^x.

Input: n = 16
Output: true

Input: n = 5
Output: false

Input: n = 1
Output: true
*/

#include <iostream>
#include <string.h>
#include <math.h>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n <= 0) return false;
        float k = log10(double(n)) / log10(double(4));
        int x = int(k);
        return bool(int(pow(4, x)) == n);
    }
};