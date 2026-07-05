# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1 = l1
        curr2 = l2

        temp = None
        while curr1 and curr2:
            # take values sume them floor and % with 10 to get carry and output

            _sum = curr1.val + curr2.val + carry

            carry = _sum // 10
            curr1.val = _sum % 10

            if curr2.next and not curr1.next:
                curr1.next = ListNode()
            if curr1.next and not curr2.next:
                curr2.next = ListNode()

            temp = curr1
            curr1 = curr1.next
            curr2 = curr2.next

        
        if carry == 0:
            return l1
        temp.next = ListNode(carry)
        return l1
        

            # if carry == 0 : return l1
            # if carry != : return l1 + new node node.val = carry

        
            