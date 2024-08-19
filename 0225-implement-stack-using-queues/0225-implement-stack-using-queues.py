class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.appendleft(x)

    def pop(self) -> int:
        N = len(self.q)
        for _ in range(N-1):
            self.q.appendleft(self.q.pop())
        x = self.q.pop()
        return x

    def top(self) -> int:
        N = len(self.q)
        for _ in range(N-1):
            self.q.appendleft(self.q.pop())
        x = self.q.pop()
        self.q.appendleft(x)
        return x       

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()