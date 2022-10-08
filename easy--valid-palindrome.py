# NeetCode's solution: 

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower()

        return newStr == newStr[::-1] 


test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panama.s"))