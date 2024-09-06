# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.mid(head)
        right.next = tmp
        right.next = None
        right = tmp

        l1 = sortList(left)
        l2 = sortList(right)

        return self.merge(l1, l2)

    def mid(head):
        slow, fast = head, head.next