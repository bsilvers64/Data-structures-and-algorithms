class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def sub(i, curr_sub):
            if i >= len(nums): 
                ans.append(curr_sub[:])
                return

            curr_sub.append(nums[i])
            sub(i+1, curr_sub)
            curr_sub.pop()
            sub(i+1, curr_sub)
            
        
        sub(0, [])
        
        return ans

        