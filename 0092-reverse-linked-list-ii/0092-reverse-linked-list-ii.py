# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr, dummy = head, ListNode(0, head)
        count = right - left + 1
        lp = dummy
        while left > 1:
            lp = curr
            curr = curr.next
            left -= 1
        
        prev = None
        
        while count:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            count -= 1
        
        lp.next.next = curr
        lp.next = prev

        return dummy.next
