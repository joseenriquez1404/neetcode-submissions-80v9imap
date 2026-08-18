class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = curr = []

        for i in range(len(nums)):
            if len(curr) == 0:
                curr.append(nums[i])
                continue

            if curr[-1] == nums[i] - 1:
                curr.append(nums[i])
            elif curr[-1] == nums[i]:
                continue
            else:
                ans = max(curr, ans, key = len)
                curr = [nums[i]]

        return len(max(ans, curr, key = len))


        