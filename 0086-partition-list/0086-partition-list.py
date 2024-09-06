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
            node = ListNode(curr.val)
            if curr.val < x:
                left.next = node
                left = node
            else:
                right.next = node
                right = node                
            curr = curr.next

        left.next = right_temp.next

        return ans.next