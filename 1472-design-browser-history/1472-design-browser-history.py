class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        node = Node(homepage)
        self.right, self.left = Node(), Node()
        node.prev, node.next = self.left, self.right
        self.right.prev = node
        self.left.next = node
        self.curr = node

    def visit(self, url: str) -> None:
        newNode = Node(url)
        newNode.next = self.right
        newNode.prev = self.curr
        self.curr.next = newNode
        self.curr = newNode
        self.right.prev = newNode

    def back(self, steps: int) -> str:
        curr = self.curr
        while curr and steps > 0:
            curr = curr.prev
            steps -= 1
        if not curr or steps < 0 or curr == self.left:
            curr = self.left.next

        self.curr = curr
        return curr.val 

    def forward(self, steps: int) -> str:
        curr = self.curr
        while curr and steps > 0:
            curr = curr.next
            steps -= 1
        if not curr or steps < 0 or curr == self.right:
            curr = self.right.prev

        self.curr = curr
        return curr.val         


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)