import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxS, minS = max(piles), 1
        ans = 1000000001
        while minS <= maxS:
            mid = (maxS + minS) // 2
            countHrs = 0
            for pile in piles:
                if pile <= mid:
                    countHrs += 1
                else:
                    countHrs += math.ceil(pile / mid)
                    
            print(countHrs)
            if countHrs <= h:
                ans = min(ans, mid)
                maxS = mid - 1
            else:
                minS = mid + 1
        
        return ans

"""
piles = [1,4,3,2]

h = 9

El rango debe estar entre la max(piles) y min(piles)

Escogo el de en medio -> checo si puedo comer todas las bananas dentro h
si -> muevo el r al mid - 1
no -> muevo l al mid + 1

regreso al final mid
"""