from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Finds the maximum path sum in a binary tree using bottom-up post-order DFS.

        Time Complexity: O(N) visits each node exactly once.
        Space Complexity: O(H) recursion call stack depth where H is tree height.
        """
        max_sum = float('-inf')

        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # Ignore negative contributions
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Price of the new path where `node` is the highest turn point
            price_newpath = node.val + left_gain + right_gain
            if price_newpath > max_sum:
                max_sum = price_newpath

            # Return max gain the node and one of its subtrees can add to ancestor
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return int(max_sum)
