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
    Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

    Input: n = 5
    Output: 10

    Input: n = 6
    Output: 6
*/

class Solution {
public:
    int smallestEvenMultiple(int n) {
        return (n % 2 == 0) ? n : 2*n;
    }
};