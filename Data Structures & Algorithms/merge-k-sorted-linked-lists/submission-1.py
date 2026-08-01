# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        
        def merge2List(head1, head2):
            if not head1:
                return head2
            elif not head2:
                return head1
            
            curr1 = head1
            curr2 = head2
            prev = None
            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    prev = curr1
                    curr1 = curr1.next
                else:
                    if not prev:
                        temp = curr2.next
                        curr2.next = curr1
                        head1 = curr2
                        prev = curr2
                        curr2 = temp
                        print(head1.val)
                    else:
                        prev.next = curr2
                        prev = curr2
                        temp = curr2.next
                        curr2.next = curr1
                        curr2 = temp

            if curr2:
                prev.next = curr2
            return head1

        h1 = lists[0]
        for i in range(1, len(lists)):
            h1  = merge2List(h1, lists[i])
        
        return h1
            


