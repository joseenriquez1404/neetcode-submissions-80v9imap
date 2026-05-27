from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashy = defaultdict()

        for num in nums:
            if num not in hashy:
                hashy[num] = 1
            else:
                hashy[num] += 1

        for v, c in hashy.items():
            if c > (len(nums) / 2):
                return v