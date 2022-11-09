# My solution
# Time: O(n)
# Space: O(1)

# class Solution:
#     def minCostClimbingStairs(self, cost: list[int]) -> int:
#         one, two = cost[-2], cost[-1]

#         for i in range(len(cost) - 3, -1, -1):
#             nextOne = cost[i]
#             temp = one
#             one = nextOne + min(one, two)
#             two = min(temp, one)

#         return min(one, two)


# Beautiful NeetCode solution:
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])


test = Solution()
print(test.minCostClimbingStairs([20, 10, 5, 15, 25, 10, 15, 5, 20, 10]))
