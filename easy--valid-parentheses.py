from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = deque()

        for c in s:
            if c in pairs:
                stack.append(pairs[c])
            else:
                if len(stack) == 0 or c != stack.pop():
                    return False

        return len(stack) == 0


test = Solution()
print(test.isValid("[[]]"))
