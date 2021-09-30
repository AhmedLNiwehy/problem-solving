"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.


Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]):
        check = {}
        result = []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        for i in nums1:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1
        for i in nums2:
            if i in check and check[i]:
                result.append(i)
                check[i] -= 1
        return result


S = Solution()

print(S.intersect([2, 2, 4, 6, 1], [2, 4, 6]))