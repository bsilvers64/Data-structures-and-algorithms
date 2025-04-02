class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = set()
        result = []

        for i in nums1:
            check.add(i)
        
        for i in nums2:
            if i in check:
                result.append(i)
                check.remove(i)

        return result