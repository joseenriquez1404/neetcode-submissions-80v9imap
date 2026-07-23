class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        temp = []

        for i in range(len(temperatures)):
            if len(temp) == 0 or temperatures[temp[-1]] >= temperatures[i]:
                temp.append(i)
            else:
                while len(temp) > 0 and temperatures[temp[-1]] < temperatures[i]:
                    last = temp.pop()
                    ans[last] = i - last
                temp.append(i)

        return ans