class TimeMap:

    def __init__(self):
        self.mp = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.mp[key]
        l, r = 0, len(values)-1
        ans = ""
        while l <= r:
            mid = (l+r)//2
            if timestamp == values[mid][1]: return values[mid][0]
            elif timestamp > values[mid][1]: 
                ans = values[mid][0]
                l = mid + 1
            else: r = mid - 1
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)