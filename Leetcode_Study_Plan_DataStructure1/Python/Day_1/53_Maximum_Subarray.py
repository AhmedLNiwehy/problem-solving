"""
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
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      for i in range(1, len(nums)):
        if nums[i - 1] > 0:
          nums[i] += nums[i - 1]
      return max(nums)


S = Solution()

print(S.maxSubArray([5, 4, -1, 7, 8]))
