"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        res =  [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
        res += [str(root.val) +'->' + path for path in self.binaryTreePaths(root.right)]
        return res