class Solution:
    def calPoints(self, operations: List[str]) -> int:
        values = []
        res = 0
        for op in operations:
            if op == "+":
                values.append(values[-1] + values[-2])
            elif op == "C":
                values.pop()
            elif op == "D":
                values.append(values[-1] * 2)
            else:
                values.append(int(op))

        return sum(values)


"""
ops=["5","-2","4","C","D","9","+","+"]

v = [5, -2, -4, 9, 5, 14]
"""