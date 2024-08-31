# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sa, sb = headA, headB
        la, lb = 0, 0
        while sa.next:
            sa = sa.next
            la += 1
        while sb.next:
            sb = sb.next
            lb += 1
        la += 1
        lb += 1

        while lb > la:
            headB = headB.next
            lb -= 1
        while la > lb:
            headA = headA.next
            la -= 1
                        
        while headA and headB:
            if headA == headB: return headA
            headA = headA.next
            headB = headB.next
            

        return None