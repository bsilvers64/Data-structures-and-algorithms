# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        max_width = 0

        queue.append([root, 1])

        while queue:
            queue_length = len(queue)
            _, first_index = queue[0]
            _, last_index = queue[-1]
            max_width = max(max_width, last_index - first_index + 1)
            while queue_length:
                node, index = queue.popleft()
                if node.left:
                    queue.append([node.left, 2*index])
                if node.right:
                    queue.append([node.right, 2*index+1])
                queue_length -= 1

        return max_width
