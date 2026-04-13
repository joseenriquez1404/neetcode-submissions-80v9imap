from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        #print(freq)

        heap = []
        for num, count in freq.items():
            #print(num, count)
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        #print(heap)
        res = []
        for count, num in heap:
            res.append(num)

        return res