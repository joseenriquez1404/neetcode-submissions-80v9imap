class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = r

        while l <= r:
            mid = (l + r) // 2
            d = 0
            suma = 0
            for i in range(len(weights)):
                if suma + weights[i] <= mid:
                    suma += weights[i]
                else:
                    d += 1
                    suma = weights[i]

            if d < days:
                ans = min(ans, mid)
                r = mid - 1 
            else:
                l = mid + 1

        return ans

        



"""
Lo minimo que podemos cargar es 1 y lo maximo
Podemos cargar más de 1 dia a la vez sin que se pase del maximo

"""