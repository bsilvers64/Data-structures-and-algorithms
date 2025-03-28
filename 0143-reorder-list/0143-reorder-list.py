# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first, second = head, slow.next
        slow.next = None

        prev, curr = None, second
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        second = prev

        toggle = 1
        while first:
            if toggle:
                temp = first.next
                first.next = second
                first = temp
                toggle = 0
            else:
                temp = second.next
                second.next = first
                second = temp
                toggle = 1

        return head