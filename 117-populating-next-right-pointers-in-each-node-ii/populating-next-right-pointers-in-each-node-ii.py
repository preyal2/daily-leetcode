class Solution:
    def connect(self, root: "Node") -> "Node":
        cur = root

        while cur:
            head = tail = None

            while cur:
                left = cur.left
                if left:
                    if head:
                        tail.next = left
                    else:
                        head = left
                    tail = left

                right = cur.right
                if right:
                    if head:
                        tail.next = right
                    else:
                        head = right
                    tail = right

                cur = cur.next

            if tail:
                tail.next = None

            cur = head

        return root