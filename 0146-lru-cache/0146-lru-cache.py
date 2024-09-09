class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.left = Node(0, None, None) 
        self.right = Node(0, self.left, None)
        self.left.next = self.right
        self.keys = {}

    def get(self, key: int) -> int:
        val = -1
        if key in self.keys:
            node = self.keys[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.right
            self.right.prev.next = node
            node.prev = self.right.prev
            self.right.prev = node

            val = self.keys[key].val[1]

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].val[1] = value
            _ = self.get(key)
        else:
            if len(self.keys) == self.size:
                del self.keys[self.left.next.val[0]]
                self.left.next = self.left.next.next
                self.left.next.prev = self.left
                
            node = Node(val=[key, value])
            node.prev = self.right.prev
            node.next = self.right
            self.right.prev.next = node
            self.right.prev = node
            self.keys[key] = node
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)