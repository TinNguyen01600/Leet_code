// Similar to problem 0724

#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
        int left_sum = 0;
        int right_sum = 0;
        for (int i = 1; i<nums.size(); i++) right_sum += nums[i];
        nums.push_back(0);
        for (int i = 0; i<nums.size() - 1; i++){
            if (left_sum == right_sum)  return i;
            else{
                left_sum += nums[i];
                right_sum -= nums[i+1];
            }
        }
        return -1;
    }
};