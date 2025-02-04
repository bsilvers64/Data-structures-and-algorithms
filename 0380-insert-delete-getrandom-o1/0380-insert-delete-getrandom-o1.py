import random
class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.num_to_index = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False
        else:
            self.nums.append(val)
            self.num_to_index[val] = len(self.nums)-1
            return True


    def remove(self, val: int) -> bool:
        if val in self.num_to_index:
            index = self.num_to_index[val] 

            self.nums[-1], self.nums[index] = self.nums[index], self.nums[-1]
            
            self.num_to_index[self.nums[index]] = index

            self.nums.pop()
            del self.num_to_index[val]
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