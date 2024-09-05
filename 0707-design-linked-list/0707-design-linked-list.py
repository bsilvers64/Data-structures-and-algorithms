class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr == None or curr == self.right:
            return -1
        return curr.val


    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val=val), self.left.next, self.left
        node.prev = prev
        node.next = next
        next.prev = node
        prev.next = node
        

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val=val), self.right, self.right.prev
        node.prev = prev
        node.next = next
        next.prev = node
        prev.next = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, next, prev = ListNode(val=val), curr, curr.prev
            node.prev = prev
            node.next = next
            next.prev = node
            prev.next = node



    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1        
        if curr and index == 0 and curr != self.right:
            prev, next = curr.prev, curr.next
            prev.next = next
            next.prev = prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)