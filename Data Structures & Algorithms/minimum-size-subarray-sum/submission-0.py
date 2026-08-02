class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = 1000001
        suma = 0
        l, r = 0, 0

        while r < len(nums):
            suma += nums[r]
            if suma >= target:
                size = min(size, r - l + 1)
                suma = 0
                l += 1
                r = l  
            else:
                r += 1

        if size == 1000001:
            return 0
        return size
        