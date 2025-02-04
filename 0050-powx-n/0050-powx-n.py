class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_negative = n < 0
        
        n = abs(n)
        memo = defaultdict(int)

        memo[0] = 1
        memo[1] = x

        def fast_pow(x, n):
            if n in memo: return memo[n]
            else:
                memo[n] = fast_pow(x, n//2) * fast_pow(x, n//2)
                if n & 1: 
                    memo[n] *= x
                    
            return memo[n]
        
        value = fast_pow(x, n)

        if is_negative:
            return 1/value
        
        return value
        
            
