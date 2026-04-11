from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = defaultdict()

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff not in hashy:
                hashy[nums[i]] = i
            else:
                return [hashy[diff], i]