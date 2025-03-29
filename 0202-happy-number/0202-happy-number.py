class Solution:
    def isHappy(self, n: int) -> bool:
        def compute_square(n):
            sum = 0
            while n:
                temp = n % 10
                sum += (temp**2)
                n //= 10
            return sum

        squares = defaultdict(int)
        
        num = n
        while num != 1:
            if num not in squares:
                squares[num] = compute_square(num)
                num = squares[num]
            else: return False

        return True