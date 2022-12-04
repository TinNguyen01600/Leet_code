#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

/*
    Given a sorted array of distinct integers and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.

    Input: nums = [1,3,5,6], target = 5
    Output: 2

    Input: nums = [1,3,5,6], target = 2
    Output: 1

    Input: nums = [1,3,5,6], target = 7
    Output: 4
*/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int k = 0;
        for (int i = 0; i<nums.size(); i++){
            if (nums[i] == target)  return i;
            if (nums[i] < target)   k = i+1;
        }
        return k;
    }
};