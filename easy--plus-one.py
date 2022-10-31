# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:
#         strList = list(map(str, digits))
#         strInt = "".join(digits)
#         strInt = str(int(integer) + 1)
#         res = []
#         for s in strInt:
#             res.append(int(s))
#         return res

# Solution #2
# Time: O(n)
# Space: O(1)

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits = digits[::-1]
        add = 1
        i = 0

        while add:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                    i += 1
                else:
                    digits[i] += add
                    add = 0
            else:
                digits.append(1)
                add = 0
        
        return digits[::-1]



test = Solution()
print(test.plusOne([4, 3, 9, 9, 9]))
