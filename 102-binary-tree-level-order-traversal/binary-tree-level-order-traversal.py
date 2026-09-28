from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        Breadth-First Search (BFS) level-order traversal using double-ended queue.

        Time Complexity: O(N) visits each node once.
        Space Complexity: O(W) maximum queue width where W <= N/2 for full binary tree.
        """
        if not root:
            return []

        levels = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(current_level)

        return levels
