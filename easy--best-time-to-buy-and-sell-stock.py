# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        r = 1
        maxP = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        
        return maxP

test = Solution()
print(test.maxProfit([1, 2, 3, 4]))