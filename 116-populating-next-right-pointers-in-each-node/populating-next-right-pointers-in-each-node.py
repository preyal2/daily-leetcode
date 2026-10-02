class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        cur = root

        while cur:
            head = tail = None

            while cur:
                left = cur.left
                if left:
                    if head is None:
                        head = left
                    else:
                        tail.next = left
                    tail = left

                right = cur.right
                if right:
                    if head is None:
                        head = right
                    else:
                        tail.next = right
                    tail = right

                cur = cur.next

            if tail:
                tail.next = None

            cur = head

        return root