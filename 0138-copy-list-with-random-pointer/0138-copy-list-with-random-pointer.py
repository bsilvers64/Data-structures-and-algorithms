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
        if not head: return None
        oldToCopy = {}
        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        node = head
        while node:
            if node.next: oldToCopy[node].next = oldToCopy[node.next]
            if node.random: oldToCopy[node].random = oldToCopy[node.random]
            node = node.next
        
        return oldToCopy[head]
        