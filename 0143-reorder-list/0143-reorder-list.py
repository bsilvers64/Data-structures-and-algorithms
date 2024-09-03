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
        list1 = head
        curr = head.next
        dummy = ListNode(head.val)
        list2 = dummy

        while curr:
            x = ListNode(curr.val)
            dummy.next = x
            dummy = x
            curr = curr.next

        prev, curr = None, list2

        N = 0
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            N += 1
        
        list2 = prev

        toggle = 1

        while N > 1:
            if toggle:
                nxt1 = list1.next
                list1.next = list2
                list1 = nxt1
                toggle = 0
            else:
                nxt2 = list2.next
                list2.next = list1
                list2 = nxt2
                toggle = 1
            N -= 1
            
        list1.next = None
        list2.next = None


        return head