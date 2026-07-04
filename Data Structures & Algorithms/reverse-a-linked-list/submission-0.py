# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = head
        prev = None
        while counter:
            temp = counter.next
            counter.next = prev
            prev = counter
            counter = temp
        
        return prev