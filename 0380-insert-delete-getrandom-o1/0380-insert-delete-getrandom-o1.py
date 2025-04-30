class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.index = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.index: return False
        self.nums.append(val)
        i = len(self.nums)-1
        self.index[val] = i
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index: return False

        i = self.index[val]
        self.index[self.nums[-1]] = i
        self.nums[-1], self.nums[i] = self.nums[i], self.nums[-1]
        self.nums.pop()

        del self.index[val]
        return True


    def getRandom(self) -> int:
        i = random.choice(self.nums)
        return i


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()