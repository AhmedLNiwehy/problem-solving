
/*
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1
*/

#include <stdio.h>
#include <stdlib.h>

int maxSubArray(int* nums, int numsSize)
{
    int i, total=0, max=INT_MIN;
    
    for(i=0; i<numsSize; i++)
    {
        total += nums[i];
        if(total > max)
            max = total;
        if(total < 0)
            total = 0;
    }
    return max;
}

int main()
{
    int arr[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int max = maxSubArray(arr, 9);
    printf("%d", max);
    return 0;
}