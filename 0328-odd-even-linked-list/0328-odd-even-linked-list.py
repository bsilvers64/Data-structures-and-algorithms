# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        elif not head.next: return head
        odd = head
        even = head.next
        even_start = head.next

        while odd.next and even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = even_start

        return head