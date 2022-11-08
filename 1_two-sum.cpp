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
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Input: nums = [3,3], target = 6
    Output: [0,1]
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        int i, j;
        int size = nums.size();
        for (i = 0; i<size-1; i++){
            for (j = i+1; j<size; j++){
                if ((nums[i] + nums[j]) == target){
                    v.push_back(i);
                    v.push_back(j);
                    continue;
                    // break;
                }
                // cout << i << " " << j << endl;
            }
            // break;
        }
        return v;
    }
};