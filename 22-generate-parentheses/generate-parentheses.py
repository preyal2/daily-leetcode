class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = [''] * (n << 1)
        N = n << 1
        append = ans.append

        def dfs(pos, l, r):
            if pos == N:
                append(''.join(path))
                return

            if l < n:
                path[pos] = '('
                dfs(pos + 1, l + 1, r)

            if r < l:
                path[pos] = ')'
                dfs(pos + 1, l, r + 1)

        dfs(0, 0, 0)
        return ans