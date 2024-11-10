class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: if s is empty or starts with '0', it can't be decoded
        if not s or s[0] == '0':
            return 0

        # DP array to store the number of ways to decode up to each index
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # An empty string has one way to be decoded
        
        # Initialization for the first character
        dp[1] = 1 if s[0] != '0' else 0

        # Fill the DP array
        for i in range(2, n + 1):
            # Single-digit decode (must be between '1' and '9')
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Two-digit decode (must be between '10' and '26')
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        # The final element of dp represents the total number of ways to decode the entire string
        return dp[n]




        