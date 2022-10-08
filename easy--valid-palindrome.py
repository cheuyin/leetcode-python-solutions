# NeetCode's solution #1:

# Time complexity: O(n)
# Space complexity: O(n)

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr = ""
#         for char in s:
#             if char.isalnum():
#                 newStr += char.lower()

#         return newStr == newStr[::-1]


# test = Solution()
# print(test.isPalindrome("A man, a plan, a canal: Panama."))


# NeetCode's solution #2

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while not self.isAlphanumeric(s[l]) and l < r:
                l += 1
            while not self.isAlphanumeric(s[r]) and r > l:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True

    def isAlphanumeric(self, c: str) -> bool:
        return ((ord("A") <= ord(c) <= ord("Z")) or
                (ord("a") <= ord(c) <= ord("z")) or
                (ord("0") <= ord(c) <= ord("9")))


test = Solution()
print(test.isPalindrome(",,,,"))
