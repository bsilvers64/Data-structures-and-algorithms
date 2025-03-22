class ListNode:
    def __init__(self, val=None, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val

class LinkedList:
    def __init__(self):
        self.map = {}
        self.left = ListNode(0)
        self.right = ListNode(0, prev=self.left)
        self.left.next = self.right

    def length(self):
        return len(self.map)

    # create a new node in the LL and push it on to the rightmost
    def push_right(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node
    
    # delete a node from the LL and from map 
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)
    
    # pop the least recently used
    def pop_left(self):
        res = self.left.next.val
        self.pop(res)
        return res
    
    # make a val as most recently used in the LL
    def update(self, val):
        self.pop(val)
        self.push_right(val)


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfu_cnt = 0
        self.val_map = {} # key -> val
        self.count_map = defaultdict(int) # key -> count
        self.list_map = defaultdict(LinkedList) # count of key -> LinkedList
    
    def counter(self, key):
        # get current count of key and increment it 
        cnt = self.count_map[key]
        self.count_map[key] += 1

        # pop this key from the previous count's linkedinlist and insert it to new one as MRU 
        self.list_map[cnt].pop(key)
        self.list_map[cnt+1].push_right(key)

        # update the lfu_count
        # if there is no node left in that count's LL, then we make LFU LL as next count
        if cnt == self.lfu_cnt and self.list_map[cnt].length() == 0:
            self.lfu_cnt += 1

    def get(self, key: int) -> int:
        if key in self.val_map: 
            self.counter(key)
            return self.val_map[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return 

        if self.cap == len(self.val_map) and key not in self.val_map:
            res = self.list_map[self.lfu_cnt].pop_left()
            self.val_map.pop(res)
            self.count_map.pop(res)

        self.val_map[key] = value
        self.counter(key)
        self.lfu_cnt = min(self.lfu_cnt, self.count_map[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)