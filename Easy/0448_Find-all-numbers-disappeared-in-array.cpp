/*
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Input: nums = [1,1]
Output: [2]
*/

#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> result;
        for (int i = 1; i<=nums.size(); i++){
            if (find(nums.begin(), nums.end(), i) == nums.end()){
                result.push_back(i);
            }
        }
        return result;
    }
};