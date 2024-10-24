class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        l, r = 0, N-1
        ans, curr = 0, 0
        people.sort()
        while l < r:
            total = people[l] + people[r]
            if total <= limit: 
                l += 1
            r -= 1
            ans += 1
        
        if l == r: ans += 1

        return ans