# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        ans = dummy
        curr = head.next
        curr_prev = head
        while curr:
            tmp = curr.next
            if curr.val >= curr_prev.val:
                curr_prev = curr
                curr = tmp
                continue

            prev, n = dummy, dummy.next
            while n != curr:
                if curr.val < n.val:
                    curr_prev.next = tmp
                    curr.next = n
                    prev.next = curr
                    curr = tmp
                    break
                prev = n
                n = n.next
            print(dummy)
            print("\n")
        
        return ans.next