class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.priority = 0

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.priority += 1
            self.cache[key][1] = self.priority


            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity and key not in self.cache:
            key_min = None
            val = float("inf")
            for k in self.cache:
                
                if val > self.cache[k][1]:
                    val = self.cache[k][1]
                    key_min = k
            
            self.cache.pop(key_min)
        
        self.priority += 1
        self.cache[key] = [value, self.priority]

