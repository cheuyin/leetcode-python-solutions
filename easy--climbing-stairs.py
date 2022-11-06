# NeetCode's solution
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one

# test = Solution()
# print(test.climbStairs(4))