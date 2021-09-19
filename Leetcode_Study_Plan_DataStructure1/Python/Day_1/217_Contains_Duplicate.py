"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = False
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                flag = True
                break
        return flag

    def containsDuplicate1(self, nums: List[int]) -> bool:
        set_version = set(nums)
        return len(set_version) != len(nums)

    def containsDuplicate2(self, nums: List[int]) -> bool:
        flag = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[i] == nums[j]:
                    flag = True
                    break
        return flag


S = Solution()

print(S.containsDuplicate2([1, 2, 0, 3]))
