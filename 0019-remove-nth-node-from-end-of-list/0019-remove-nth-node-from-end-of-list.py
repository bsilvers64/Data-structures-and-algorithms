# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right, left = head, head

        while right and n:
            right = right.next
            n -= 1

        if not right:
            head = head.next
            return head
        
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next


        return head