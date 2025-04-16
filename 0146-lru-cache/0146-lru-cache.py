class ListNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        
        # left most node represent the least recently used value
        self.left = ListNode()

        # right most nodes represent the most recently used value
        self.right = ListNode()

        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}


    def remove(self, key):
        ''' this function ejects a node from the linked list'''
        if key in self.cache:
            prevnode, nextnode = self.cache[key].prev, self.cache[key].next
            prevnode.next = nextnode
            nextnode.prev = prevnode
            del self.cache[key]


    def remove_lru(self):
        ''' this function ejects the least recently used node from the left'''
        self.remove(self.left.next.key)


    def insert(self, key, val):
        ''' this function inserts a node to the right-most, making it 
            the most recently used '''
        self.remove(key)
        node = ListNode(key, val, prev=self.right.prev, next=self.right)
        node.prev.next = node
        self.right.prev = node
        self.cache[key] = node


    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self.insert(key, val)
            return val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        self.insert(key, value)
        if len(self.cache) > self.cap:
            self.remove_lru()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)