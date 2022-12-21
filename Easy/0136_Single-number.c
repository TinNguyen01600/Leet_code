/*
    Given a non-empty array of integers nums, every element appears twice except for one. 
    Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.

    Input: nums = [2,2,1]
    Output: 1

    Input: nums = [2,2,1]
    Output: 1

    Input: nums = [1]
    Output: 1
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int singleNumber(int* nums, int numsSize){
    int *freq;
    int len_freq = 60000;
    freq = (int*)calloc(len_freq, sizeof(int));
    for (int i = 0; i<numsSize; i++)    freq[nums[i] + 30000]++;
    for (int i = 0; i<len_freq; i++){
        if (freq[i] == 1)   return i - 30000;
    }
    return 0;
}