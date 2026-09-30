from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """
        Reconstructs binary tree using hash map for O(1) inorder index lookups.

        Time Complexity: O(N) where N is the number of nodes.
        Space Complexity: O(N) hash map storage and recursion call stack.
        """
        inorder_idx_map = {val: i for i, val in enumerate(inorder)}
        preorder_idx = 0

        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_idx
            if left > right:
                return None

            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            preorder_idx += 1

            mid = inorder_idx_map[root_val]
            root.left = array_to_tree(left, mid - 1)
            root.right = array_to_tree(mid + 1, right)

            return root

        return array_to_tree(0, len(inorder) - 1)
