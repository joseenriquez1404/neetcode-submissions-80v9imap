class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operators = "+*/-"
        for t in tokens:
            if t not in operators:
                nums.append(int(t))
            else:
                if t == "+":
                    val1 = nums.pop()
                    val2 = nums.pop()
                    nums.append(val1 + val2)
                elif t == "-":
                    val1 = nums.pop()
                    val2 = nums.pop()
                    nums.append(val2 - val1)
                elif t == "*":
                    val1 = nums.pop()
                    val2 = nums.pop()
                    nums.append(val1 * val2)
                else:
                    val1 = nums.pop()
                    val2 = nums.pop()
                    nums.append(int(val2 / val1))
        return nums[0]

        