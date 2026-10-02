class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        cur = root

        while cur:
            next_head = None
            next_tail = None

            while cur:
                left = cur.left
                if left:
                    if next_head is None:
                        next_head = left
                    else:
                        next_tail.next = left
                    next_tail = left

                right = cur.right
                if right:
                    if next_head is None:
                        next_head = right
                    else:
                        next_tail.next = right
                    next_tail = right

                cur = cur.next

            if next_tail:
                next_tail.next = None

            cur = next_head

        return root