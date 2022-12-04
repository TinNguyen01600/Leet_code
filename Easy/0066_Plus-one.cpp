#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <string.h>
#include <vector>
#include <conio.h>
#include <list>
#include <unordered_map>
#include <stdlib.h>
#include <set>
#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

/*
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
    Increment the large integer by one and return the resulting array of digits.

    Input: digits = [1,2,3]
    Output: [1,2,4]

    Input: digits = [9]
    Output: [1,0]
*/

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int len = digits.size();
        int r[len];
        vector<int> result;
        int n = 1;

        for (int i = len-1; i>=0; --i){
            r[i] = digits[i] + n;
            if(r[i] > 9)  {r[i] %= 10; n = 1;}
            else n = 0;
        }
        if (n == 1) result.push_back(1);
        for (int i = 0; i<len; i++) result.push_back(r[i]);
        return result;
    }
};