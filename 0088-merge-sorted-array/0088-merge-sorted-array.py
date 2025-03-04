class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m+n-1
        i, j = m-1, n-1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
        
        # if num1 elements are over but num2s are left, we put those remaining ones in nums1
        # otherwise if num2s are over it means, the rest is already sorted.

        while j >= 0:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1
        