from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashy = defaultdict()
        for i in range(len(nums)):
            if nums[i] in hashy:
                for j in hashy[nums[i]]:
                    diff = abs(i - j)
                    if diff <= k:
                        return True
                hashy[nums[i]].append(i)
            else:
                hashy[nums[i]] = [i]

        return False
        