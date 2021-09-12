"""
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        low = 0
        high = len(nums) - 1
        res = -1
        while low <= high:                  # searching for the first position
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                res = mid
                high = mid - 1              # move to the left towards the smallest position
        result.append(res)

        low = 0
        high = len(nums) - 1
        res = -1
        while low <= high:                  # searching for the last position
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                res = mid
                low = mid + 1               # move to the right towards the smallest pos
        result.append(res)
        return result


S = Solution()
print(S.searchRange([7,7,8,8,8,10,10,10], 10))