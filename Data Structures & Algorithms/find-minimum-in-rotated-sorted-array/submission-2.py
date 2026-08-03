class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = 1001

        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
                m = min(m, nums[mid])
        return m
        
"""
[3,4,5,6,1,2]
[1,2,3,4,5,6]

l = 3 r = 2


"""