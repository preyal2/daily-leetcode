class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    O(1) Least Recently Used Cache combining Hash Map and Doubly Linked List.

    Time Complexity: O(1) for both get and put operations.
    Space Complexity: O(capacity) storing up to capacity key-node pairs.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: DLinkedNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLinkedNode):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node: DLinkedNode):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DLinkedNode:
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)
