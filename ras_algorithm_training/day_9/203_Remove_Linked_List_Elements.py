"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list
that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []
"""

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        prev = None
        while (temp != None and temp.val == val):
            head = temp.next
            temp = head

        while temp:
            while temp and temp.val != val:
                prev = temp
                temp = temp.next
            if temp == None:
                return head
            prev.next = temp.next
            temp = prev.next
        return head