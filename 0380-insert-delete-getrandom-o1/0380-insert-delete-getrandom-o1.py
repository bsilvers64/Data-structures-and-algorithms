class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indices = defaultdict(int)


    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        else:
            index = len(self.nums)
            self.nums.append(val)
            self.indices[val] = index
            return True


    def remove(self, val: int) -> bool:
        if val in self.indices:
            index = self.indices[val]
            self.indices[self.nums[-1]] = index
            self.nums[-1], self.nums[index] = self.nums[index], self.nums[-1]
            self.nums.pop()
            del self.indices[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()