# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left, right = head, head
        n = k

        while k > 1:
            left = left.next
            right = right.next
            k -= 1 
        
        right = left.next
        
        curr = head
        while right:
            curr = curr.next
            right = right.next
        
        right = curr

        left.val, right.val = right.val, left.val

        return head