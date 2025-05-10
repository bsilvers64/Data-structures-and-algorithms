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
        queue.appendleft(root)

        result = []
        flag = 1

        while queue:
            level = deque()
            for _ in range(len(queue)):
                node = queue.pop()

                if flag: level.appendleft(node.val)
                else: level.append(node.val)

                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

            flag = 1 if not flag else 0
            temp = []
            while level: temp.append(level.pop())
            result.append(temp)


        return result