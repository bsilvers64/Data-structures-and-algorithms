# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 1
        if not head: return head

        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        
        k %= n
        if n == 1 or n == k or not k: return head

        
        count = n - k - 1

        curr = head
        while count:
            curr = curr.next
            count -= 1
        
        temp = curr.next
        curr.next = None
        tail.next = head
        head = temp
        

        return head