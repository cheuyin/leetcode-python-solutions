# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        visited = {}
        for i in nums:
            if i in visited:
                return True
            else:
                visited[i] = True
        return False