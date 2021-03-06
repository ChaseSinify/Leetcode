"""
Given the root of a Binary Search Tree (BST), 
convert it to a Greater Tree such that every key 
of the original BST is changed to the original key plus 
sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Note: This question is the same as 538: 
https://leetcode.com/problems/convert-bst-to-greater-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.runningSum = 0
        self.dfs(root)
        return root
    def dfs(self, root):
        """Function completes reversed inorder traversal, adds to running sum"""
        if root:
            self.dfs(root.right)
            root.val = self.runningSum = self.runningSum + root.val
            self.dfs(root.left)
        
    # @lee215's solution that is much cleaner than mine
    # def bstToGst(self, root):
    #     if root.right: self.bstToGst(root.right)
    #     root.val = self.val = self.val + root.val
    #     if root.left: self.bstToGst(root.left)
    #     return root
        
