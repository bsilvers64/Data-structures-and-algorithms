class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # index from the last of the result array
        index = m+n-1

        i = m-1
        j = n-1

        # we fill the last, whichever element is larger and move from last to first
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
        
        # in case if we finished the nums1 array but nums2 array is still left
        # that means remaining nums2 elements are smaller so we just fill the 
        # rest of the array nums1

        # if nums2 finished first, we don't do anything because nums1 is already sorted then

        while j >= 0:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1
        