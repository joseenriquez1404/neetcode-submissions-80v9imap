class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [], []
        before = 1
        for num in nums:
            left.append(before)
            before = before * num
        before = 1
        for i in range(len(nums) - 1, -1, -1):
            right.append(before)
            before = before * nums[i]

        right = right[::-1]

        for i in range(len(left)):
            left[i] = left[i] * right[i]

        return left
        