class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head, self.tail = Node(0), Node(0)
        self.head.next = self.tail
        self.tail.next = self.head
        self.capacity = k
        self.curr_len = 0

    def enQueue(self, value: int) -> bool:
        if self.curr_len < self.capacity:
            node = Node(value)
            if self.tail:
                self.tail.next = node
                self.tail = node
            else:
                head, tail = node, node
            self.curr_len += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.head:
            if self.head == self.tail:
                self.tail = self.tail.next
            self.head = self.head.next 
            self.curr_len -= 1

            return True
        else:
            return False
        
    def Front(self) -> int:
        if self.head:
            return self.head.val

    def Rear(self) -> int:
        if self.tail:
            return self.tail.val

    def isEmpty(self) -> bool:
        if self.curr_len == 0: return True
        else: return False

    def isFull(self) -> bool:
        if self.curr_len == self.capacity: return True
        else: return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()