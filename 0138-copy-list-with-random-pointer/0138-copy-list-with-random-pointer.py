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

        # hash-map that maps old node to newly created node
        listmap = defaultdict(Node)

        # creating the new linked list and inserting the kye-value pairs in our listmap
        curr = head
        while curr:
            newNode = Node(x = curr.val)
            listmap[curr] = newNode
            curr = curr.next

        # now we assign the next and the random pointer of the nodes in our new linked list 
        for oldNode, newNode in listmap.items():
            if oldNode.next: newNode.next = listmap[oldNode.next]
            else: newNode.next = None    
            if oldNode.random: newNode.random = listmap[oldNode.random]
            else: newNode.random = None
        
        return listmap[head]
        