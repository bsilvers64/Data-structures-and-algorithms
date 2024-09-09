# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, l: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(l) == 1: return l[0]
        elif not l: return None
        n = len(l)
        left = self.mergeKLists(l[:n//2])
        right = self.mergeKLists(l[n//2:])
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = temp = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2

        return dummy.next