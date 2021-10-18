"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
Example :
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

TODO : find an O(n) solution using a different approach
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return (nums)


S = Solution()

print(S.sortedSquares([-4, -5, 1, 2, 7, 3]))