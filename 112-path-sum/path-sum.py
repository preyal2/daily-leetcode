class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, targetSum)]

        while stack:
            node, remaining = stack.pop()
            remaining -= node.val

            if node.left is None and node.right is None:
                if remaining == 0:
                    return True
                continue

            if node.right:
                stack.append((node.right, remaining))

            if node.left:
                stack.append((node.left, remaining))

        return False