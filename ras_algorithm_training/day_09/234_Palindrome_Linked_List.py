"""
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true\

Example 2:
Input: head = [1,2]
Output: false
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        stack = []

        while temp:
            if temp.next:
                stack.append(head.val)
                temp = temp.next
            head = head.next
            temp = temp.next

        while head:
            if stack.pop() != head.val:
                return False
            head = head.next

        return True