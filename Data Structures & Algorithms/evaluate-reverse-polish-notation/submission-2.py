class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for t in tokens:
            if t not in "+*-/":
                nums.append(int(t))
            else:
                val1 = nums.pop()
                val2 = nums.pop()
                if t == "+":
                    nums.append(val2 + val1)
                if t == "-":
                    nums.append(val2 - val1)
                if t == "*":
                    nums.append(val2 * val1)
                if t == "/":
                    nums.append(int(val2 / val1))

        return nums.pop()

        