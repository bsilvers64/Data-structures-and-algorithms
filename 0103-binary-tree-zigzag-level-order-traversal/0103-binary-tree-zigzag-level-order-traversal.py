# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque()
        queue.append(root)

        result = []
        left_to_right = True

        while queue:
            level = deque()
            for _ in range(len(queue)):
                node = queue.pop()

                if left_to_right:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)

                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

            left_to_right = not left_to_right
            temp = []
            while level:
                temp.append(level.pop())
            result.append(temp)

        return result