# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        num = n
        l = 1

        while l <= num:
            mid = (l + num) // 2
            val = guess(mid)
            if val == 0:
                return mid
            elif val == -1:
                num = mid - 1
            else:
                l = mid + 1
        