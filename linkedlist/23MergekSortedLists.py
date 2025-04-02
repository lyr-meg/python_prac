# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        dummy = ListNode()
        tail = dummy

        for x in sorted(nodes):
            tail.next = ListNode(x)
            tail = tail.next
            
        return dummy.next

# Time complexity : O(NlogN) where N is the total number of nodes
# Space complexity : O(N)