# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, sA: ListNode, sB: ListNode) -> Optional[ListNode]:  
        headA, headB = sA, sB
        while headA != headB:
            headA = headA.next if headA else sB
            headB = headB.next if headB else sA

        return headA