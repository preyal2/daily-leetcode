from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """
        Bidirectional Breadth-First Search (BFS) finding the shortest word transformation sequence.

        Time Complexity: O(M^2 * N) where M is word length and N is wordList size.
        Space Complexity: O(M * N) for the word dictionary set and bidirectional frontiers.
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        begin_set = {beginWord}
        end_set = {endWord}
        length = 1

        while begin_set and end_set:
            # Always expand smaller frontier
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_set = set()
            for word in begin_set:
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch == word[i]:
                            continue
                        next_word = word[:i] + ch + word[i+1:]
                        if next_word in end_set:
                            return length + 1
                        if next_word in word_set:
                            next_set.add(next_word)
                            word_set.remove(next_word)

            begin_set = next_set
            length += 1

        return 0
