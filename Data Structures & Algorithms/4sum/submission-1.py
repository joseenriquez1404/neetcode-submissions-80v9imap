class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums = sorted(nums)
        n = len(nums)

        ans = set()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                l, r = j + 1, n - 1
                while l < r:
                    suma = nums[i] + nums[j] + nums[l] + nums[r]
                    if suma == target:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif suma < target:
                        l += 1
                    else:
                        r -= 1

        return [list(t) for t in ans]


"""
[3,2,3,-3,1,0] 
1. Primero lo puedo ordenar
[-3, 0, 1, 2, 3, 3]
 l               r  
2. Hago 2 punteros l y r en 0 y len(nums) - 1 y otros dos l2 y r2 en l2 = l + 1 y r2 = r - 1


"""