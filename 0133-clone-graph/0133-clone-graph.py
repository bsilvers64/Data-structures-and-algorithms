"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        q = collections.deque()
        
        if not node: return None

        visited[node] = Node(node.val)
        q.append(node)

        while q:
            root = q.pop()
            for neighbor in root.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.appendleft(neighbor)
                visited[root].neighbors.append(visited[neighbor])
        
        return visited[node]