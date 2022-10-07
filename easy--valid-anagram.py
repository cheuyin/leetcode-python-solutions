# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        # Count every letter in s
        for i in s:
            if not (i in letters):
                letters[i] = 1
            else:
                letters[i] += 1
        # Count every letter in t
        for j in t:
            if not(j in letters):
                return False
            else:
                letters[j] -= 1
        # Check if anagram
        for key in letters:
            if letters[key] != 0:
                return False
        print(letters)
        return True


# NeetCode's solution:
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[i] = 1 + countS.get(i, 0)
#             countT[i] = 1 + countT.get(i, 0)
#         for j in countT:
#             if countT[j] != countS.get(j, 0):
#                 return False 
#         return True
