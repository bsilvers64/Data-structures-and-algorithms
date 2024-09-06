# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        left = ans = ListNode()
        right = right_temp = ListNode()
        while curr:
            if curr.val < x:
                left.next = curr
                left = curr
            else:
                right.next = curr
                right = curr
            curr = curr.next

        left.next = right_temp.next
        right.next = None

        return ans.next
