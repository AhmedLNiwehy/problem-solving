"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example :
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int):
        for i in range(k):
            nums.insert(0, nums[len(nums) - 1])
            nums.pop(len(nums) - 1)
        return nums

    def rotate1(self, nums: List[int], k: int):
        to_rotate = nums[-k:]
        nums = to_rotate + nums[:-k]
        return nums

    def rotate2(self, nums: List[int], k: int):
        while k != 0:
            index = len(nums) - 1
            temp = nums[index]
            for i in range(index):
                nums[index - i] = nums[index - (i+1)]
            nums[0] = temp
            k -= 1
        return nums


S = Solution()
print(S.rotate([1, 3, 5, 7, 9, 11], 3))