class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        cur = root

        while cur is not None:
            head = None
            tail = None

            while cur is not None:
                node = cur.left
                if node is not None:
                    if head is None:
                        head = node
                    else:
                        tail.next = node
                    tail = node

                node = cur.right
                if node is not None:
                    if head is None:
                        head = node
                    else:
                        tail.next = node
                    tail = node

                cur = cur.next

            if tail is not None:
                tail.next = None

            cur = head

        return root