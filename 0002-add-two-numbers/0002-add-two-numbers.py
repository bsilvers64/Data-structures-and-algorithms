# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def numerize(head):
            ans, i = 0, 1
            while head:
                ans += (head.val*i)
                i *= 10
                head = head.next
            return ans
        
        total = numerize(l1) + numerize(l2)
        if not total: return ListNode()
        head = ListNode()
        curr = head
        num, i = 0, 1
        while total: 
            node = ListNode(val=total % 10)
            curr.next = node
            curr = node
            total //= 10


        
        return head.next