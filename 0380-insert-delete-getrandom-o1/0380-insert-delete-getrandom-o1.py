class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            self.nums.append(val)
            self.indices[val] = len(self.nums)-1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.indices:
            index_to_remove = self.indices[val]
            self.nums[index_to_remove] = self.nums[-1]
            self.indices[self.nums[-1]] = index_to_remove
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