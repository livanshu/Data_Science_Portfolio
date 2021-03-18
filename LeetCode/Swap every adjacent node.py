# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        a = ListNode(0)
        a.next = head
        b = a
        while b.next != None and b.next.next:
            n1 = b.next
            n2 = b.next.next
            b.next = n2
            n1.next = n2.next
            n2.next = n1
            b = n1
        return a.next
        
