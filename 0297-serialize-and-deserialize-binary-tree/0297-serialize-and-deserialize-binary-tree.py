# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def preorder(self, root, tree):
        if not root:
            tree.append("N")
            return
        tree.append(str(root.val))
        self.preorder(root.left, tree)
        self.preorder(root.right, tree)

    def build_tree(self, tree):
        if tree[self.i] == "N":
            self.i += 1
            return None
        node = TreeNode(int(tree[self.i]))
        self.i += 1
        node.left = self.build_tree(tree)
        node.right = self.build_tree(tree)
        return node

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = []
        self.preorder(root, tree)
        return ",".join(tree)        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        tree = data.split(",")
        return self.build_tree(tree)
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))