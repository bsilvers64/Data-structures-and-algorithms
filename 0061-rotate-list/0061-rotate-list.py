# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 1

        if not head: return None

        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        
        k %= length
        tail = curr

        if length == 1 or length == k or not k: return head
        
        n = length-k-1
        curr = head
        while n:
            curr = curr.next
            n -= 1
        
        tail.next = head
        head = curr.next
        curr.next = None

        return head