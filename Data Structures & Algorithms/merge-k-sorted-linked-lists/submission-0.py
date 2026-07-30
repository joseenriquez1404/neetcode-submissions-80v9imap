# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return 

        ans = lists[0] # Se crea una lista base

        def merge_lists(l1, l2):
            h1, h2 = l1, l2
            c = ans = ListNode()

            while h1 and h2:
                if h1.val <= h2.val:
                    ans.next = h1
                    h1 = h1.next
                else:
                    ans.next = h2
                    h2 = h2.next

                ans = ans.next

            if h1:
                ans.next = h1
            else:
                ans.next = h2
            return c.next


        for i in range(1, len(lists)):
            ans = merge_lists(ans, lists[i])

        return ans


"""
[[1,2,4],[1,3,5],[3,6]]
            ^
a -> 1 -> 2 -> 4 -> None
                ^
"""
       