# Last updated: 3/1/2026, 12:16:54 PM
# used DFS, could also solve this using BFS since DFS would only work for small trees if the tree had like 50,000 nodes this approach would probably get a stack overflow since it doesn't store the data in heap memory like BFS.
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        def dfs(root):
10            if not root: #check to see if we're in the root and to ensure its not empty
11                return 0 #if we are then return 0
12            return max(dfs(root.left), dfs(root.right)) + 1 #call our function recursively to travel through both the left and the right branches
13        
14        return dfs(root)
15        