# # Resursive solution
# # Time: O(n)
# # Space: O(n)
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0 
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Iterative BFS solution
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0 
        
#         level = 0
#         q = deque([root])
#         while q:
#             for i in range(len(q)):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
            
#             level += 1
        
#         return level 

# Iterative DFS solution 
class Solution: 
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        stack = [[root, 1]]
        res = 1 

        while stack:
            node, depth = stack.pop()
            if node: 
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return res
        




