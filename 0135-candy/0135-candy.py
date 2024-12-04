class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        if N == 1: return 1
        candies = [1] * N
    
        # this makes sure that every kid that more candies that their left neighbor
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        print(candies)
        # this makes sure every kid has more candies than their right neighbor
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        print(candies)
        return sum(candies)
