class Node:
    def __init__(self, data=None, key= None):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None

    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = 0
        self._map = {}


        self.head = Node(-1,-1)
        self.end = Node(-1,-1)
        self.end.prev = self.head
        self.head.next = self.end

    def get(self, key: int) -> int:
        if key not in self._map:
            return -1
        
        node = self._map[key]
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        return node.data

    def put(self, key: int, value: int) -> None:

        # cur = self.head
        # while cur:
        #     print(cur.data)
        #     cur = cur.next
        # print("-----------------",key,value)
        
        # if key already in map part
        if key in self._map:
            node = self._map[key]
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            head_next_node = self.head.next
            node.next = head_next_node
            node.prev = self.head

            self.head.next.prev = node
            self.head.next = node

            node.data = value
            
            return None
        
        if self.items == self.capacity:
            prev_node = self.end.prev

            prev_prev_node = prev_node.prev

            prev_prev_node.next = self.end
            self.end.prev = prev_prev_node

            prev_node.next = None
            prev_node.prev = None

            del self._map[prev_node.key]

            self.items -= 1


        if key not in self._map:
            next_node = self.head.next
            node = Node(value, key)

            self._map[key] = node

            node.next = next_node
            node.prev = self.head

            next_node.prev = node
            self.head.next = node

            self.items += 1

