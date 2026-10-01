class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Captures surrounded regions by marking boundary-connected 'O's via DFS.

        Time Complexity: O(M * N) where M is rows and N is columns.
        Space Complexity: O(M * N) recursion stack in worst case.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'E'  # Mark as escaped / border-connected
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Traverse borders and mark all connected 'O's as 'E'
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # 2. Flip surrounded 'O's to 'X', restore 'E's back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
