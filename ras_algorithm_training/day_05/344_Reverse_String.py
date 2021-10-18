"""
Write a function that reverses a string. The input string is given as an array of characters s.

Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            (s[i], s[len(s) - (i + 1)]) = (s[len(s) - (i + 1)], s[i])
        return s

    def reverseString2(self, s: List[str]) -> None:
        s.reverse()
        return s


S = Solution()
print(S.reverseString(["h", "e", "l", "l", "o"]))