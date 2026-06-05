class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r:
            suma = numbers[l] + numbers[r]
            if suma == target:
                return [l + 1, r + 1]
            elif suma > target:
                r -= 1
            else:
                l += 1