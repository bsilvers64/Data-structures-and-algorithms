class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix_products = [1] * (N+1)
        suffix_products = [1] * (N+1)
        products = []

        for i in range(N):
            prefix_products[i+1] = nums[i] * prefix_products[i]
            suffix_products[N-i-1] = nums[N-i-1] * suffix_products[N-i]

        for i in range(N):
            products.append(prefix_products[i] * suffix_products[i+1]) 
        
        return products