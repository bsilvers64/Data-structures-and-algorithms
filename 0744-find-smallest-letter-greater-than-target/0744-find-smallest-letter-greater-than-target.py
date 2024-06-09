class Solution:
    def nextGreatestLetter(self, letters: List[str], t: str) -> str:
        start, end = 0, len(letters)-1
        res = -1
        
        while start <= end:
            mid = (start + end)//2
            if letters[mid] == t: 
                start = mid + 1
            elif t < letters[mid]: 
                res = mid
                end = mid - 1
            else: start = mid + 1

        if res == -1: return letters[0]
        return letters[res]