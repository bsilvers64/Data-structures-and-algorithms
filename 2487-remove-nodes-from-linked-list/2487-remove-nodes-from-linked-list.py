# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            curr, prev = head, None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        head = reverse(head)

        curr = head
        curr_max = ListNode()
        ans = curr_max
        while curr:
            if curr.val >= curr_max.val:
                dummy = ListNode(val=curr.val)
                curr_max.next = dummy
                curr_max = dummy
            curr = curr.next
            #print(curr_max)
        
        
        ans = reverse(ans.next)
        return ans