class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        for l in range(len(nums)):
            if nums[l] not in seen:
                seen.add(nums[l])
            else:
                for r in range(l + 1, len(nums)):
                    if nums[r] not in seen:
                        seen.add(nums[r])
                        nums[l], nums[r] = nums[r], nums[l]
                        break
        return len(seen)


"""
[2,10,30,10,30,30]
             l
                r

(2, 10, 30)
"""