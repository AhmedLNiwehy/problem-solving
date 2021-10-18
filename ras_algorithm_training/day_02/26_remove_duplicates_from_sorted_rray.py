"""
Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements
of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        index = 0
        peak = nums[index]
        for i in range(1, len(nums)):
            if nums[i] > peak:
                peak = nums[i]
                index += 1
                nums[index] = nums[i]
        return index + 1


S = Solution()

print(S.removeDuplicates([1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8]))