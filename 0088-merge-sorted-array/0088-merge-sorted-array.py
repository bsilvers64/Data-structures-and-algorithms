class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not m: 
            nums1[0] = nums2[0]
            exit
        
        r1, r2 = m-1, n-1
        r = m+n-1
        while r1 >= 0 and r2 >= 0:
            if nums1[r1] > nums2[r2]:
                nums1[r] = nums1[r1]
                r1 -= 1
            else:
                nums1[r] = nums2[r2]
                r2 -= 1
            r -= 1
        