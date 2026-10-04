class MinStack:
    """
    Constant time O(1) min stack pairing values with running minimums.

    Time Complexity: O(1) for push, pop, top, and getMin.
    Space Complexity: O(N) auxiliary memory for paired stack.
    """
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
