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
        
        slow, fast = n, n
        while fast != 1:
            slow = compute_square(slow)
            fast = compute_square(fast)
            fast = compute_square(fast)
            if slow == fast and slow != 1: return False

        return True