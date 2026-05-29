from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashy = defaultdict()

        for num in nums:
            if num not in hashy:
                hashy[num] = 1
            else:
                hashy[num] += 1

        ordenado = dict(sorted(hashy.items(), key=lambda x: x[1], reverse = True))
        return list(ordenado.keys())[:k]

        