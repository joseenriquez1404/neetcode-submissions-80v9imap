"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashy = {}

        curr = head
        while curr != None:
            hashy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        newH = Node(1)
        ans = newH
        while curr != None:
            newH.next = hashy[curr]
            if curr.random != None:
                newH.next.random = hashy[curr.random]
            else:
                newH.next.random = None
            newH = newH.next
            curr = curr.next

        return ans.next
        
"""
1. Guardar los nodos dentro de un hashmap

Luego al crear la lista apuntar el nodo random a los nodos que estan dentro del hashmap.
"""
        




