#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long
/*  
    Given an integer x, return true if x is a palindrome, and false otherwise.
    Input: x = 121
    Output: true

    Input: x = -121
    Output: false

    Input: x = 10
    Output: false
*/
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)  return false;
        else{
            int temp = x;
            unsigned int y = 0, r;
            while (temp != 0){
                y *= 10;
                r = temp%10;
                y += r;
                temp /= 10;
            }
            if (x == y)  return true;
            else    return false;
        }
    }
};