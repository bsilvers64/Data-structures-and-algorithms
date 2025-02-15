from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = ListNode()
        dummy = curr
        heap = []
        for i in range(len(lists)):
            head = lists[i]
            if head: heappush(heap, (head.val, i, head))
        
        while heap:
            _, i, node = heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node: heappush(heap, (node.val, i, node))
        
        return dummy.next