class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        top_span = 0
        while self.st and price >= self.st[-1][0]:
            top_price, span = self.st.pop()
            top_span += span
        self.st.append([price, top_span+1])
        return self.st[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)