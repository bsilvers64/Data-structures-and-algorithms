class ListNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.map = {} # maps ListNode value to the node in the Linked-list
        self.right = ListNode(0)
        self.left = ListNode(0, next=self.right)
        self.right.prev = self.left

    def length(self):
        """ returns the current length of the linked-list """
        return len(self.map)

    def push_right(self, val):
        """ creates a new node and inserts it to the right most of the linked-list 
            making it as Most-Recently-Used node """
        
        node = ListNode(val, prev = self.right.prev, next = self.right)
        self.map[val] = node
        next, prev = self.right, self.right.prev
        prev.next = node
        next.prev = node
    
    def pop(self, val):
        """ removes a node from the map as well as the linked-list """
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            prev.next = next
            next.prev = prev
            self.map.pop(val, None)
    
    def pop_left(self):
        """" removes the least recently used node - from the left most 
            and returns the value """
        res = self.left.next.val
        self.pop(res)
        return res
    
    def update(self, val):
        """ making any value node as the most recently used inthe linked-list"""
        self.pop(val)
        self.push_right(val)


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfu_count = 0
        self.value_map = {}                     # maps key to value
        self.count_map = defaultdict(int)       # maps key to a count
        self.list_map = defaultdict(LinkedList)   # maps count to its LinkedList

    def counter(self, key):
        """ updates the count of any key, removes that key from the linked list
            of that count, then increments the count and inserts this key to the
            linked-list of that new count """

        # get the current count of this key
        count = self.count_map[key]
        
        # increment the count of this key
        self.count_map[key] += 1

        # remove it from the linked list of previous count
        self.list_map[count].pop(key)

        # add it to the linkedlist of new count
        self.list_map[count + 1].push_right(key)

        # update the LFU count if previous count was the LFU count and its 
        # linked list became empty now
        if self.lfu_count == count and self.list_map[count].length() == 0:
            self.lfu_count += 1


    def get(self, key: int) -> int:
        """ gets the key's value if it exists and increments its frequency count """
        if key in self.value_map:
            self.counter(key)
            return self.value_map[key]
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        
        """ inserts the new key to its count's linkedlist and evicts the least frequently
            used key (and the least recently used) key in case capacity reached"""

        if self.cap == len(self.value_map) and key not in self.value_map:
            res = self.list_map[self.lfu_count].pop_left()
            self.value_map.pop(res)
            self.count_map.pop(res)

        self.value_map[key] = value
        self.counter(key)
        self.lfu_count = min(self.lfu_count, self.count_map[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)