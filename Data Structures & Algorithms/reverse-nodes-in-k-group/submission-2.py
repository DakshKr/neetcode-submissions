# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # 1. Reverse the whole Linked List and count total nodes (n)
        n = 0
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n += 1

        # 2. Reverse the first (n % k) elements again ONLY if a remainder exists
        i = n % k
        prev1 = None
        
        if i > 0:
            curr1 = prev
            start = prev
            while curr1 and i > 0:
                temp = curr1.next
                curr1.next = prev1
                prev1 = curr1
                curr1 = temp
                i -= 1
            if start:
                start.next = curr1
        
        # If n < k, no segments of length k exist; return the modified list
        if n < k: 
            return prev1 if prev1 else prev
        
        # 3. Collect the (start, end) boundaries for each segment
        newHead = prev1 if prev1 else prev
        l1 = [(None, None)]  # Base padding for your stitching logic
        newCurr = newHead
        i2 = n % k
    
        # Handle the remainder segment boundary safely
        if i2 > 0:
            rem_start = newCurr
            for _ in range(i2 - 1):
                newCurr = newCurr.next
            rem_end = newCurr
            l1.append((rem_start, rem_end))
            newCurr = newCurr.next
        
        # Handle the standard k-group segment boundaries safely
        while newCurr:
            group_start = newCurr
            for _ in range(k - 1):
                if newCurr:
                    newCurr = newCurr.next
            group_end = newCurr
            l1.append((group_start, group_end))
            if newCurr:
                newCurr = newCurr.next
        
        # 4. Stitch the segments back together in reverse order
        for x in range(len(l1) - 1, 0, -1):
            s, e = l1[x]
            e.next = l1[x-1][0]
        
        return l1[-1][0]