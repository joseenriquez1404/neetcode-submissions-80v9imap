# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        nodes = []
        while curr != None:
            nodes.append(curr)
            curr = curr.next

        while left <= right:
            aux = nodes[right - 1].val
            nodes[right - 1].val = nodes[left - 1].val
            nodes[left - 1].val = aux
            left += 1
            right -= 1

        return head