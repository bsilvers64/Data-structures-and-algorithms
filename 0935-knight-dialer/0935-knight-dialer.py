class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        neighbors = {
            0:(4,6),
            1:(6,8),
            2:(7,9),
            3:(4,8),
            4:(0,3,9),
            5:(),
            6:(0,1,7),
            7:(2,6),
            8:(1,3),
            9:(2,4)
            }

        for _ in range(n-1):
            temp = [0] * 10
            for j in range(10):
                # num of ways to get to j
                for k in neighbors[j]:
                    temp[k] = (temp[k] + dp[j]) % (10**9+7)
            dp = temp
        
        ans = 0
        for i in dp:
            ans = (ans + i) % (10**9+7)
        return ans
