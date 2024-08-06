class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = collections.defaultdict(int)
        i, j, ans = 0, 0, 0

        N = len(fruits)
        while (i < N):
            basket[fruits[i]] += 1
            while len(basket) > 2:
                basket[fruits[j]] -= 1
                if not basket[fruits[j]]: del basket[fruits[j]]
                j += 1
            ans = max(ans, i - j + 1)
            i += 1
        return ans