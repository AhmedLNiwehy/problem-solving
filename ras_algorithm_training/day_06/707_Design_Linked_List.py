"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node
in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:
MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion,
the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
If index equals the length of the linked list, the node will be appended to the end of the linked list.
If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Example:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your val structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        temp = self.head
        if temp is None:
            return -1
        i = 0
        while temp is not None and i < index:
            temp = temp.next
            i += 1
        if temp is None:
            return -1
        return temp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        new_node.next = None
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        i = 0
        temp = self.head
        while temp is not None and i < index - 1:
            temp = temp.next
            i += 1
        if temp is None:
            return
        new_node.next = temp.next
        temp.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head is None:
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
            return
        i = 0
        while temp is not None and i < index - 1:
            temp = temp.next
            i += 1
        if temp is None or temp.next is None:
            return
        temp1 = temp.next
        temp.next = temp1.next

    def Display(self):
        temp = self.head
        ll = []
        while temp is not None:
            ll.append(temp.val)
            temp = temp.next
        return ll


ll = MyLinkedList()
ll.addAtHead(10)
ll.addAtTail(20)
ll.addAtIndex(1, 12)
print(ll.Display())
print(ll.get(1))
ll.deleteAtIndex(1)
print(ll.Display())
