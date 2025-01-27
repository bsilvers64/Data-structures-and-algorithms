from heapq import heappop, heappush

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            value, i, node = heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heappush(heap, (node.val, i, node))

        return dummy.next