from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque([0])

        for i in range(1, len(temperatures)):
            while (len(stack) > 0) and temperatures[i] > temperatures[stack[0]]:
                result[stack[0]] =  i - stack[0]
                stack.popleft()

            stack.appendleft(i)
        return result


"""
temperatures[i] -> Temperatura del dia i

[30,38,30,36,35,40,28]
                ^

[35, 36, 38]
[1,0, 1,0,0,0,0]
"""