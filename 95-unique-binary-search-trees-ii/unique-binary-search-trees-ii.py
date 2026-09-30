class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        from functools import cache

        @cache
        def dfs(l, r):
            if l > r:
                return (None,)

            res = []

            for v in range(l, r + 1):
                left = dfs(l, v - 1)
                right = dfs(v + 1, r)

                for a in left:
                    for b in right:
                        res.append(TreeNode(v, a, b))

            return tuple(res)

        return list(dfs(1, n))