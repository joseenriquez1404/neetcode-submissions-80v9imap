from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.lrucache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
        else:
            return -1
        return self.lrucache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
        self.lrucache[key] = value
        if len(self.lrucache) > self.capacity:
            self.lrucache.popitem(last = False)
            
        
