# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head

        while curr != None:
            nodes.append(curr)
            curr = curr.next

        if n == len(nodes):
            return head.next

        pos = len(nodes) - n -1 
        nodes[pos].next = nodes[pos].next.next
        return head
        