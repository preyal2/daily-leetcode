class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)

        # Count minimum removals needed.
        lrem = rrem = 0
        balance = 0

        for c in s:
            if c == '(':
                balance += 1
            elif c == ')':
                if balance:
                    balance -= 1
                else:
                    rrem += 1

        lrem = balance

        ans = set()
        path = []

        def dfs(i, bal, left, right):
            if n - i < left + right:
                return

            if i == n:
                if left == 0 and right == 0 and bal == 0:
                    ans.add(''.join(path))
                return

            c = s[i]

            if c == '(':
                # Remove '('
                if left:
                    dfs(i + 1, bal, left - 1, right)

                # Keep '('
                path.append(c)
                dfs(i + 1, bal + 1, left, right)
                path.pop()

            elif c == ')':
                # Remove ')'
                if right:
                    dfs(i + 1, bal, left, right - 1)

                # Keep ')' only when it has a matching '('
                if bal:
                    path.append(c)
                    dfs(i + 1, bal - 1, left, right)
                    path.pop()

            else:
                # Keep non-parenthesis characters.
                path.append(c)
                dfs(i + 1, bal, left, right)
                path.pop()

        dfs(0, 0, lrem, rrem)
        return list(ans)