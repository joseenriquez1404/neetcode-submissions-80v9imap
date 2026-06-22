from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        openC = "({["
        stack = deque()

        for c in s:
            if c in openC:
                stack.append(c)
            else:
                if len(stack) > 0:
                    if c == ")" and stack[-1] == "(":
                        stack.pop()
                    elif c == "]" and stack[-1] == "[":
                        stack.pop()
                    elif c == "}" and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return len(stack) == 0
