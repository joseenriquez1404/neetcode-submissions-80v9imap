class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = float('-inf')

        if x == 0:
            return 0
        if x == 1:
            return 1

        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x < ((mid + 1) * (mid + 1)):
                ans = max(ans, mid)
                l += 1
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
        return ans