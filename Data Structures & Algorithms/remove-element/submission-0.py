class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            print(num)
            if num != val:
                nums[k] = num
                k += 1

        print(f"k = {k} and nums = {nums}")
        return k