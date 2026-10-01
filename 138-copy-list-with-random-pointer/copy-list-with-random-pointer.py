from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        """
        Deep copies linked list with random pointers in O(1) space via node interleaving.

        Time Complexity: O(N) three-pass traversal.
        Space Complexity: O(1) auxiliary space (excluding cloned nodes).
        """
        if not head:
            return None

        # Pass 1: Clone nodes and interleave: A -> A' -> B -> B'
        curr = head
        while curr:
            cloned = Node(curr.val, curr.next, None)
            curr.next = cloned
            curr = cloned.next

        # Pass 2: Assign random pointers for cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Pass 3: Separate original and cloned linked lists
        curr = head
        pseudo_head = Node(0)
        copy_curr = pseudo_head

        while curr:
            next_orig = curr.next.next
            copy = curr.next
            copy_curr.next = copy
            copy_curr = copy

            curr.next = next_orig
            curr = next_orig

        return pseudo_head.next
