""""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that
the majority element always exists in the array.

Example:
Input: nums = [3,2,3]
Output: 3
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums)//2
        return nums[mid]


S = Solution()
print(S.majorityElement([1, 2, 1]))
