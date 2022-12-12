/*
    Given an integer array nums and an integer val, 
    remove all occurrences of val in nums in-place. 
    The relative order of the elements may be changed.
    Return k after placing the final result in the first k slots of nums.
    
    int[] nums = [...]; // Input array
    int val = ...; // Value to remove
    int[] expectedNums = [...]; // The expected answer with correct length.
                                // It is sorted with no values equaling val.
    int k = removeElement(nums, val); // Calls your implementation
    assert k == expectedNums.length;
    sort(nums, 0, k); // Sort the first k elements of nums
    for (int i = 0; i < actualLength; i++) {
        assert nums[i] == expectedNums[i];
    }

    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]

    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]
*/
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

int removeElement(vector<int>& nums, int val) {
    int len = nums.size();
    vector<int> a, b;
    for (int i = 0; i<len; i++){
        if (nums[i] == val)     a.push_back(nums[i]);
        else    b.push_back(nums[i]);
    }
    nums = b;
    nums.insert(nums.end(), a.begin(), a.end());
    return b.size();
}

int main(void){
    vector<int> nums = {0,1,2,2,3,0,4,2};
    int val = 2;
    int k = removeElement(nums, val);
    for (auto i = 0; i<nums.size(); i++){
        cout << nums[i] << " ";
    }
}