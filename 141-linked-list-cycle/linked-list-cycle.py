from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects cycle using Floyd's Tortoise and Hare two-pointer algorithm.

        Time Complexity: O(N) where N is number of nodes.
        Space Complexity: O(1) constant auxiliary space.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
