from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        Zigzag level-order traversal using BFS and double-ended queue.

        Time Complexity: O(N) where N is number of nodes in the binary tree.
        Space Complexity: O(W) where W is maximum width of the tree (at most N/2).
        """
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = deque()

            for _ in range(level_size):
                node = queue.popleft()
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(current_level))
            left_to_right = not left_to_right

        return result
