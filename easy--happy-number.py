# My solution

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         results = {}

#         while True:
#             res = 0
#             for i in str(n):
#                 res += int(i)**2
#                 print(i)

#             if res == 1:
#                 return True
#             elif res in results:
#                 return False
#             else:
#                 results[res] = True
#                 n = res

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False

    def sumOfSquares(self, n: int) -> int:
        squareSum = 0

        while n:
            lastDigit = n % 10
            squareSum += lastDigit ** 2
            n = n // 10

        return squareSum


test = Solution()
test.isHappy(19)
