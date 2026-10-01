from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Calculates sum of all root-to-leaf numbers using pre-order DFS.

        Time Complexity: O(N) traversing all nodes in the tree.
        Space Complexity: O(H) recursion stack proportional to tree height H.
        """
        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            # Leaf node reached
            if not node.left and not node.right:
                return current_sum

            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)
