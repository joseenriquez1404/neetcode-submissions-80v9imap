class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1], [1]
        before = 1
        for i in range(1, len(nums)):
            left.append(nums[i - 1] * before)
            before = nums[i - 1] * before

        before = 1
        for i in range(len(nums) - 2, -1, -1):
            right.insert(0, nums[i + 1] * before)
            before = nums[i + 1] * before

        return [left[i] * right[i] for i in range(len(left))]

"""
[1, 2, 4, 6]

l = [1, 1, 2, 8]
r = [48 ,24,6, 1]


"""

        