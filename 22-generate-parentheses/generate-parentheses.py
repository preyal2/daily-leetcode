class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = [''] * (n * 2)

        def dfs(pos, left, right):
            if pos == n * 2:
                ans.append(''.join(path))
                return

            if left < n:
                path[pos] = '('
                dfs(pos + 1, left + 1, right)

            if right < left:
                path[pos] = ')'
                dfs(pos + 1, left, right + 1)

        dfs(0, 0, 0)
        return ans