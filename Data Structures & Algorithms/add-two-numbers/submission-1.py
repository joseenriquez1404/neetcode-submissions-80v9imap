# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = l1, l2
        r = ha = ListNode()
        s = 0

        while c1 and c2:
            # print(f"c1: {c1.val} c2: {c2.val}")
            suma = s + c1.val + c2.val
            if suma > 9:
                ha.next = ListNode(suma - 10)
                s = 1
            else:
                ha.next = ListNode(suma)
                s = 0
            ha = ha.next
            c1 = c1.next
            c2 = c2.next

        if c1:
            while c1:
                # print(f"2c1: {c1.val}")
                suma = s + c1.val
                if suma > 9:
                    ha.next = ListNode(suma - 10)
                    s = 1
                else:
                    ha.next = ListNode(suma)
                    s = 0
                c1 = c1.next
                ha = ha.next
        
        if c2:
            while c2:
                # print(f"2c2: {c2.val}")
                suma = s + c2.val
                if suma > 9:
                    ha.next = ListNode(suma - 10)
                    s = 1
                else:
                    ha.next = ListNode(suma)
                    s = 0
                ha = ha.next
                c2 = c2.next

        if s > 0:
            ha.next = ListNode(s)
        return r.next

"""
Steps:
1. Tengo que ir recorriendo hasta que se acabe la primera lista
2. Sumo los dos valores de cada nodo
    Lo maximo que pueden sumar es 18 porque 9 + 9
    entonces debo de llevar un contador del extra y sumarlo 
3. Si queda una lista la termino de sumar 
4. Sumo el sobrante

"""