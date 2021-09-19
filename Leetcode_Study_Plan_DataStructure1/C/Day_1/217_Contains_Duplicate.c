/*
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false
*/


int comp (const int *a, const int *b) 
{
   return (*a - *b);
}

bool containsDuplicate(int* nums, int numsSize)
{
    bool flag = false;
    qsort(nums, numsSize, sizeof(int), comp);
    for (int i = 0; i < numsSize - 1; i++) 
    {
        if (nums[i] == nums[i+1])
        {
            flag = true;
            break;
        }
    }
    return flag;
}