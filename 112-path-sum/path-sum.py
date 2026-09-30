from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Validates existence of root-to-leaf path sum using depth-first search.

        Time Complexity: O(N) in worst case visiting all nodes.
        Space Complexity: O(H) recursion call stack depth where H is tree height.
        """
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
