class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum)]

        while stack:
            node, s = stack.pop()
            s -= node.val

            left = node.left
            right = node.right

            if left is None and right is None:
                if s == 0:
                    return True
                continue

            if left is not None:
                stack.append((left, s))

            if right is not None:
                stack.append((right, s))

        return False