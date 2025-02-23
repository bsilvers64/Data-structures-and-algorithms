from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        
        dummy = ListNode()
        curr = dummy
        heap = []

        # pushing the starting nodes of all linked-lists to min-heap
        for index, first_node in enumerate(lists):
            if first_node:
                heappush(heap, [first_node.val, index, first_node])
        
        # popping nodes one-by-one from heap and adding their next nodes
        while heap:
            _, index, node = heappop(heap)

            # pointing the previous node's next to this node
            curr.next = node

            # if next node afte this node exists, push to heap
            if node.next:
                next_node = node.next
                heappush(heap, [next_node.val, index, next_node])
            
            # make this node as current
            curr = node
        
        return dummy.next
                
