class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        largest_integer = self._mergeSort(nums, 0, len(nums)-1)
        return "0" if largest_integer[0] == "0" else "".join(largest_integer)

    def _mergeSort(self, nums, l, r):
        if l >= r: return [nums[l]]
        mid = (l+r)//2

        left = self._mergeSort(nums, l, mid)
        right = self._mergeSort(nums, mid+1, r)

        return self._merge(left, right)
    
    def _merge(self, arr1, arr2):
        i1, i2 = 0, 0
        res = []

        while i1 < len(arr1) and i2 < len(arr2):
            if self._compare(arr1[i1], arr2[i2]):
                res.append(arr1[i1])
                i1 += 1
            else:
                res.append(arr2[i2])
                i2 += 1
        
        while i1 < len(arr1):
            res.append(arr1[i1])
            i1 += 1

        while i2 < len(arr2):
            res.append(arr2[i2])
            i2 += 1

        return res
    
    def _compare(self, a, b):
        return str(a)+str(b) > str(b)+str(a)

