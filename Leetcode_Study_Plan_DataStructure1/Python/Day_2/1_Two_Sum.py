"""
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hist = {}
        for i, num in enumerate(nums):
            if target - num in hist:
                return [hist[target - num], i]
            hist[num] = i

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    return [i, j]
                    


S = Solution()
print(S.twoSum([1, 2, 4, 6, 8, 10], 11))
