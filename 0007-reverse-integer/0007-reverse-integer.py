class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        sign = 1 if x > 0 else -1
        x *= -1 if x < 0 else 1
        while x:
            num = num * 10 + (x % 10)
            x //= 10
        
        num *= sign

        if -2**31 <= num <= 2**31-1:
            return num
        else:
            return 0