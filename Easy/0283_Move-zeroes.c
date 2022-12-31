/*
    Given an integer array nums, move all 0's to the end of it 
    while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Input: nums = [0]
    Output: [0]
*/

void swap(int *a,int *b){
	int k=*a;
	*a=*b;
	*b=k;
}
void moveZeroes(int* nums, int numsSize){
    for (int i = 0; i<numsSize; i++){
        for (int j = i+1; j < numsSize; j++){
            if (nums[i] == 0 && nums[j] != 0)  swap(&nums[i], &nums[j]);
        }
    }
}