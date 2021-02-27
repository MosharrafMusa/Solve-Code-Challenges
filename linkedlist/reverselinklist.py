# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        current = head
        previous = None
        nextnode = None

        while current:
            nextnode = current.next
            current.next = previous
            previous = current
            current = nextnode

        return previous
