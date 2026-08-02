class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr

        distances = []
        for num in arr:
            distances.append((num, abs(num - x)))

        distances = sorted(distances, key = lambda x: x[1])
        return sorted([x[0] for x in distances][:k])

        

"""
dis = [4, 2, 1, 2]
"""

        