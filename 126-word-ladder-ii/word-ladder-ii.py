from collections import defaultdict
from typing import List


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        words = set(wordList)

        if endWord not in words:
            return []

        words.discard(beginWord)

        parents = defaultdict(list)
        level = {beginWord}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        found = False

        while level and not found:
            nxt_level = set()

            for word in level:
                chars = list(word)

                for i, old in enumerate(chars):
                    for c in alphabet:
                        if c == old:
                            continue

                        chars[i] = c
                        nxt = ''.join(chars)

                        if nxt in words:
                            parents[nxt].append(word)
                            nxt_level.add(nxt)

                            if nxt == endWord:
                                found = True

                    chars[i] = old

            words.difference_update(nxt_level)
            level = nxt_level

        if not found:
            return []

        ans = []
        path = [endWord]
        append = ans.append

        def dfs(word):
            if word == beginWord:
                append(path[::-1])
                return

            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)
        return ans