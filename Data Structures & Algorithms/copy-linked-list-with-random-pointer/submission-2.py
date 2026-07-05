"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        cur = head
        while cur:
            newNode = Node(cur.val)
            hashmap[cur] = newNode
            cur = cur.next

        
        cur2 = head
        while cur2:
            deepNode = hashmap[cur2]
            deepNext = None
            deepRandom = None
            
            if cur2.next:
                deepNext = hashmap[cur2.next]
            if cur2.random:
                deepRandom = hashmap[cur2.random]

            deepNode.next = deepNext
            deepNode.random = deepRandom

            cur2 =cur2.next

        if head :
            return hashmap[head]
        return None 
