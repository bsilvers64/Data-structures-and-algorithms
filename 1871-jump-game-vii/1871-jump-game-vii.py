class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = collections.deque()
        farthest = 0

        q.append(0)

        while q:
            i = q.popleft()
            l, r = max(farthest+1, i+minJump), min(i+maxJump, len(s)-1)
            for j in range(l, r+1): 
                if s[j] == "0":
                    q.append(j)
                    if j == len(s)-1: return True
            farthest = i + maxJump 
        return False
        