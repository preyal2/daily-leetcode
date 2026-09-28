from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Computes maximum root-to-leaf depth via post-order depth-first search.

        Time Complexity: O(N) traverses every node in the binary tree.
        Space Complexity: O(H) recursion stack where H is the tree height.
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
