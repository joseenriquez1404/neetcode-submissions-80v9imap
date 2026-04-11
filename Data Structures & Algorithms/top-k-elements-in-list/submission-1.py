from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Primero obtenemos las frecuencias
        freq = Counter(nums)
        
        # Implementamos un min-heap
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        # Imprimimos el resultado
        result = []
        for count, num in heap:
            result.append(num)

        return result