class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strmap = {s for s in nums}
        
        def backtrack(index, curr):
            if index == len(nums):
                res = "".join(curr)
                return None if res in strmap else res
            
            res = backtrack(index+1, curr)
            if res: return res

            curr[index] = "1"
            res = backtrack(index+1, curr)
            if res: return res

        return backtrack(0, ["0" for s in nums])