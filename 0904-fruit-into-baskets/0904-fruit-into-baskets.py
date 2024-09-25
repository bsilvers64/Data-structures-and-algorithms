class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mp = collections.defaultdict(int)
        i, j, ans = 0, 0, 0
        while j < len(fruits):
            mp[fruits[j]] += 1
            while len(mp) > 2:
                mp[fruits[i]] -= 1
                if mp[fruits[i]] == 0: del mp[fruits[i]]
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans
