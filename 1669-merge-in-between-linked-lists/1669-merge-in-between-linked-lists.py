# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2end = list2
        dummy = list1
        diff = b-a+1

        while list2end.next:
            list2end = list2end.next
        
        if a: a-= 1
        while a:
            dummy = dummy.next
            a -= 1
        

        dummy2 = dummy

        while diff:
            dummy2 = dummy2.next
            diff -= 1
        
        dummy.next= list2

        list2end.next = dummy2.next

        return list1
