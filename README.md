# 🚀 Daily LeetCode — High-Performance Algorithmic Solutions

<div align="center">

[![LeetCode](https://img.shields.io/badge/LeetCode-Solutions-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Problems Solved](https://img.shields.io/badge/Problems_Solved-240-success?style=for-the-badge)](#-complete-problem-catalog)
[![Automation](https://img.shields.io/badge/LeetSync-CI%2FCD_Automated-blueviolet?style=for-the-badge&logo=githubactions&logoColor=white)](#-automated-leetsync-pipeline)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)](./CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  <b>A curated repository of 240+ daily LeetCode solutions engineered with Python 3.12, strict Big-O complexity proofs, top-percentile runtime optimizations, and automated LeetSync synchronization.</b>
</p>

</div>

---

## 📌 Technical Overview & Engineering Standards

This repository serves as a systematic, continuous algorithmic practice vault designed for Tier-1 and FAANG technical interviews. Every solution in this repository adheres to high software engineering standards:

- **⚡ Sub-Millisecond Execution**: Solutions target 0ms (99th–100th percentile) runtime by leveraging optimal data structures (`collections.deque`, `heapq`, `bisect`, bitwise manipulation).
- **⏱️ Formal Complexity Bounds**: Every algorithm is designed to meet strict upper-bound asymptotic time complexity ($O(1)$, $O(\log N)$, or $O(N)$) and minimal auxiliary space overhead.
- **🛡️ Edge Case Resilience**: Explicit boundary testing for empty sets, null pointers, integer overflows, duplicate elements, and extreme constraints.
- **🤖 Automated Synchronization**: Integrated with **LeetSync** for automated bi-directional commit logging from live LeetCode submissions directly to GitHub.

---

## 📊 Summary & Progress Metrics

<div align="center">

| Difficulty Level | Problems Solved | Distribution | Status Badge |
| :--- | :---: | :---: | :--- |
| **🟢 Easy** | **57** | 23.8% | `![](https://img.shields.io/badge/-Easy_57-brightgreen)` |
| **🟡 Medium** | **138** | 57.5% | `![](https://img.shields.io/badge/-Medium_138-orange)` |
| **🔴 Hard** | **45** | 18.8% | `![](https://img.shields.io/badge/-Hard_45-red)` |
| **🏆 Total Solved** | **240** | **100%** | `![](https://img.shields.io/badge/-240_Total-blue)` |

</div>

---

## 🧩 Point-to-Point Algorithmic Classification Matrix

The **240 solved problems** in this repository span the following core computational paradigms:

| Algorithmic Domain | Key Underlying Principles | Representative Solved Problems |
| :--- | :--- | :--- |
| **⚡ Arrays, Hashing & Two Pointers** | Fast element lookup in $O(1)$, frequency counters, bidirectional inward convergence. | [#1 Two Sum](https://leetcode.com/problems/two-sum), [#11 Container With Most Water](https://leetcode.com/problems/container-with-most-water), [#15 3Sum](https://leetcode.com/problems/3sum), [#75 Sort Colors](https://leetcode.com/problems/sort-colors), [#88 Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array), [#118 Pascal's Triangle](https://leetcode.com/problems/pascals-triangle), [#119 Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii), [#122 Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii), [#125 Valid Palindrome](https://leetcode.com/problems/valid-palindrome), [#128 Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence), [#153 Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) |
| **🪟 Sliding Window & Substrings** | Dynamic subarray resizing, frequency map state tracking, character boundary optimization. | [#3 Longest Substring](https://leetcode.com/problems/longest-substring-without-repeating-characters), [#76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring), [#1208 Max Nesting Depth](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings), [#1298 Reverse Substrings Between Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses) |
| **🔗 Linked Lists & Pointer Arithmetic** | Sentinel dummy heads, in-place node reversals, fast & slow tortoise-hare pointers. | [#2 Add Two Numbers](https://leetcode.com/problems/add-two-numbers), [#61 Rotate List](https://leetcode.com/problems/rotate-list), [#82 Remove Duplicates II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii), [#86 Partition List](https://leetcode.com/problems/partition-list), [#92 Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii), [#109 Sorted List to BST](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree), [#138 Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer), [#141 Linked List Cycle](https://leetcode.com/problems/linked-list-cycle), [#142 Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii), [#143 Reorder List](https://leetcode.com/problems/reorder-list), [#146 LRU Cache](https://leetcode.com/problems/lru-cache), [#148 Sort List](https://leetcode.com/problems/sort-list), [#206 Reverse Linked List](https://leetcode.com/problems/reverse-linked-list) |
| **🌲 Binary Trees & Heaps** | DFS/BFS tree traversals, BST validation, min/max heap priority queues, path sums. | [#94 Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal), [#98 Validate BST](https://leetcode.com/problems/validate-binary-search-tree), [#100 Same Tree](https://leetcode.com/problems/same-tree), [#101 Symmetric Tree](https://leetcode.com/problems/symmetric-tree), [#102 Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal), [#103 Zigzag Level Order](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal), [#105 Tree from Preorder & Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal), [#106 Tree from Inorder & Postorder](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal), [#108 Sorted Array to BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree), [#110 Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree), [#111 Min Depth](https://leetcode.com/problems/minimum-depth-of-binary-tree), [#112 Path Sum](https://leetcode.com/problems/path-sum), [#113 Path Sum II](https://leetcode.com/problems/path-sum-ii), [#114 Flatten Binary Tree](https://leetcode.com/problems/flatten-binary-tree-to-linked-list), [#124 Binary Tree Max Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum), [#129 Sum Root to Leaf](https://leetcode.com/problems/sum-root-to-leaf-numbers) |
| **🔄 Backtracking & Recursion** | State-space exploration, branch pruning, constraint validation, combinatorial generation. | [#39 Combination Sum](https://leetcode.com/problems/combination-sum), [#46 Permutations](https://leetcode.com/problems/permutations), [#51 N-Queens](https://leetcode.com/problems/n-queens), [#77 Combinations](https://leetcode.com/problems/combinations), [#78 Subsets](https://leetcode.com/problems/subsets), [#90 Subsets II](https://leetcode.com/problems/subsets-ii), [#93 Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses), [#131 Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning) |
| **📈 Dynamic Programming** | Memoization, bottom-up tabulation, optimal substructure, DAG transitions. | [#53 Maximum Subarray](https://leetcode.com/problems/maximum-subarray), [#62 Unique Paths](https://leetcode.com/problems/unique-paths), [#64 Min Path Sum](https://leetcode.com/problems/minimum-path-sum), [#72 Edit Distance](https://leetcode.com/problems/edit-distance), [#87 Scramble String](https://leetcode.com/problems/scramble-string), [#91 Decode Ways](https://leetcode.com/problems/decode-ways), [#97 Interleaving String](https://leetcode.com/problems/interleaving-string), [#115 Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences), [#120 Triangle](https://leetcode.com/problems/triangle), [#123 Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii), [#139 Word Break](https://leetcode.com/problems/word-break), [#152 Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray), [#198 House Robber](https://leetcode.com/problems/house-robber) |
| **🌐 Graph Theory & Grid Traversal** | Breadth-First Search (BFS), Depth-First Search (DFS), topological sort, binary lifting, grid components. | [#79 Word Search](https://leetcode.com/problems/word-search), [#127 Word Ladder](https://leetcode.com/problems/word-ladder), [#130 Surrounded Regions](https://leetcode.com/problems/surrounded-regions), [#133 Clone Graph](https://leetcode.com/problems/clone-graph), [#200 Number of Islands](https://leetcode.com/problems/number-of-islands), [#2349 Valid Parentheses Path](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path), [#2582 Minimum Score Path](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities), [#3852 Path Existence Queries II](https://leetcode.com/problems/path-existence-queries-in-a-graph-ii) |
| **🔢 Math, Bitwise, Greedy & Stacks** | Bit manipulation, Gray codes, GCD/Euclidean algorithms, monotonic stacks, greedy gas stations. | [#7 Reverse Integer](https://leetcode.com/problems/reverse-integer), [#43 Multiply Strings](https://leetcode.com/problems/multiply-strings), [#67 Add Binary](https://leetcode.com/problems/add-binary), [#89 Gray Code](https://leetcode.com/problems/gray-code), [#134 Gas Station](https://leetcode.com/problems/gas-station), [#135 Candy](https://leetcode.com/problems/candy), [#136 Single Number](https://leetcode.com/problems/single-number), [#137 Single Number II](https://leetcode.com/problems/single-number-ii), [#150 Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation), [#155 Min Stack](https://leetcode.com/problems/min-stack), [#1737 Max Nesting Depth](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses), [#4248 Count Commas II](https://leetcode.com/problems/count-commas-in-range-ii) |

---

## 🎯 Point-to-Point Problem-Solving Standards (The 5-Step Rubric)

Every solution follows a rigorous engineering standard:

1. **Input Boundary Validation**: Explicit verification of array length limits ($N=0, N=1$), negative numbers, and boundary conditions.
2. **Invariant Discovery**: Uncovering sorted order, prefix sum relationships, monotonic sequences, or frequency constraints.
3. **Data Structure Optimization**: Replacing $O(N)$ searches with $O(1)$ Hash Maps, $O(\log N)$ Binary Search, or $O(1)$ Double-Ended Queues (`collections.deque`).
4. **Pruning & Early Termination**: Halting backtracking branches immediately when candidate paths exceed current optimal bounds.
5. **Time & Space Documentation**: Each code file contains formal Big-O asymptotic complexity analysis in its docstring.

---

## 🔄 Automated LeetSync Pipeline

```
┌───────────────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐
│     LeetCode Platform     │ ──►  │      LeetSync Engine      │ ──►  │      GitHub Repository    │
│ Accepted Submission (0ms) │      │ Automated Code Packaging  │      │ Clean Commit with Metrics │
└───────────────────────────┘      └───────────────────────────┘      └───────────────────────────┘
```

- When a problem is marked **Accepted** on LeetCode, LeetSync automatically extracts the solution, execution speed, and memory usage.
- The solution is packaged into a self-contained problem directory with complete markdown problem statement and clean `.py` implementation.
- Automatically commits with author attribution (`Modi Preyal <modipreyal@gmail.com>`), contributing directly to the GitHub activity streak.

---

## 📂 Repository Directory Structure

```text
daily-leetcode/
├── 1-two-sum/
│   ├── README.md                              # Problem statement, examples & constraints
│   └── two-sum.py                             # Optimal Python 3.12 implementation
├── 124-binary-tree-maximum-path-sum/
│   ├── README.md
│   └── binary-tree-maximum-path-sum.py
├── 138-copy-list-with-random-pointer/
│   ├── README.md
│   └── copy-list-with-random-pointer.py
├── 139-word-break/
│   ├── README.md
│   └── word-break.py
├── 155-min-stack/
│   ├── README.md
│   └── min-stack.py
├── CONTRIBUTING.md                            # Guidelines for community contributions
└── README.md                                  # Complete repository documentation & catalog
```

---

## 📝 Complete Problem Catalog (240 Solved)

| # | Problem Title | Difficulty | Language | Solution File |
| :-: | :--- | :-: | :-: | :--- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`two-sum.py`](./1-two-sum/two-sum.py) |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`add-two-numbers.py`](./2-add-two-numbers/add-two-numbers.py) |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`longest-substring-without-repeating-characters.py`](./3-longest-substring-without-repeating-characters/longest-substring-without-repeating-characters.py) |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`median-of-two-sorted-arrays.py`](./4-median-of-two-sorted-arrays/median-of-two-sorted-arrays.py) |
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`longest-palindromic-substring.py`](./5-longest-palindromic-substring/longest-palindromic-substring.py) |
| 6 | [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`zigzag-conversion.py`](./6-zigzag-conversion/zigzag-conversion.py) |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`reverse-integer.py`](./7-reverse-integer/reverse-integer.py) |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`palindrome-number.py`](./9-palindrome-number/palindrome-number.py) |
| 10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`regular-expression-matching.py`](./10-regular-expression-matching/regular-expression-matching.py) |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`container-with-most-water.py`](./11-container-with-most-water/container-with-most-water.py) |
| 12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`integer-to-roman.py`](./12-integer-to-roman/integer-to-roman.py) |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`roman-to-integer.py`](./13-roman-to-integer/roman-to-integer.py) |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`longest-common-prefix.py`](./14-longest-common-prefix/longest-common-prefix.py) |
| 15 | [3Sum](https://leetcode.com/problems/3sum) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`3sum.py`](./15-3sum/3sum.py) |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`3sum-closest.py`](./16-3sum-closest/3sum-closest.py) |
| 17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`letter-combinations-of-a-phone-number.py`](./17-letter-combinations-of-a-phone-number/letter-combinations-of-a-phone-number.py) |
| 18 | [4Sum](https://leetcode.com/problems/4sum) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`4sum.py`](./18-4sum/4sum.py) |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`remove-nth-node-from-end-of-list.py`](./19-remove-nth-node-from-end-of-list/remove-nth-node-from-end-of-list.py) |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`valid-parentheses.py`](./20-valid-parentheses/valid-parentheses.py) |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`merge-two-sorted-lists.py`](./21-merge-two-sorted-lists/merge-two-sorted-lists.py) |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`generate-parentheses.py`](./22-generate-parentheses/generate-parentheses.py) |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`merge-k-sorted-lists.py`](./23-merge-k-sorted-lists/merge-k-sorted-lists.py) |
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`swap-nodes-in-pairs.py`](./24-swap-nodes-in-pairs/swap-nodes-in-pairs.py) |
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`reverse-nodes-in-k-group.py`](./25-reverse-nodes-in-k-group/reverse-nodes-in-k-group.py) |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`remove-duplicates-from-sorted-array.py`](./26-remove-duplicates-from-sorted-array/remove-duplicates-from-sorted-array.py) |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`remove-element.py`](./27-remove-element/remove-element.py) |
| 28 | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`find-the-index-of-the-first-occurrence-in-a-string.py`](./28-find-the-index-of-the-first-occurrence-in-a-string/find-the-index-of-the-first-occurrence-in-a-string.py) |
| 29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`divide-two-integers.py`](./29-divide-two-integers/divide-two-integers.py) |
| 30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`substring-with-concatenation-of-all-words.py`](./30-substring-with-concatenation-of-all-words/substring-with-concatenation-of-all-words.py) |
| 31 | [Next Permutation](https://leetcode.com/problems/next-permutation) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`next-permutation.py`](./31-next-permutation/next-permutation.py) |
| 32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`longest-valid-parentheses.py`](./32-longest-valid-parentheses/longest-valid-parentheses.py) |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`search-in-rotated-sorted-array.py`](./33-search-in-rotated-sorted-array/search-in-rotated-sorted-array.py) |
| 34 | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`find-first-and-last-position-of-element-in-sorted-array.py`](./34-find-first-and-last-position-of-element-in-sorted-array/find-first-and-last-position-of-element-in-sorted-array.py) |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`search-insert-position.py`](./35-search-insert-position/search-insert-position.py) |
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`valid-sudoku.py`](./36-valid-sudoku/valid-sudoku.py) |
| 37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`sudoku-solver.py`](./37-sudoku-solver/sudoku-solver.py) |
| 38 | [Count and Say](https://leetcode.com/problems/count-and-say) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`count-and-say.py`](./38-count-and-say/count-and-say.py) |
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`combination-sum.py`](./39-combination-sum/combination-sum.py) |
| 40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`combination-sum-ii.py`](./40-combination-sum-ii/combination-sum-ii.py) |
| 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`first-missing-positive.py`](./41-first-missing-positive/first-missing-positive.py) |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`trapping-rain-water.py`](./42-trapping-rain-water/trapping-rain-water.py) |
| 43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`multiply-strings.py`](./43-multiply-strings/multiply-strings.py) |
| 44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`wildcard-matching.py`](./44-wildcard-matching/wildcard-matching.py) |
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`jump-game-ii.py`](./45-jump-game-ii/jump-game-ii.py) |
| 46 | [Permutations](https://leetcode.com/problems/permutations) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`permutations.py`](./46-permutations/permutations.py) |
| 47 | [Permutations II](https://leetcode.com/problems/permutations-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`permutations-ii.py`](./47-permutations-ii/permutations-ii.py) |
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`rotate-image.py`](./48-rotate-image/rotate-image.py) |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`group-anagrams.py`](./49-group-anagrams/group-anagrams.py) |
| 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`powx-n.py`](./50-powx-n/powx-n.py) |
| 51 | [N-Queens](https://leetcode.com/problems/n-queens) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`n-queens.py`](./51-n-queens/n-queens.py) |
| 52 | [N-Queens II](https://leetcode.com/problems/n-queens-ii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`n-queens-ii.py`](./52-n-queens-ii/n-queens-ii.py) |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`maximum-subarray.py`](./53-maximum-subarray/maximum-subarray.py) |
| 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`spiral-matrix.py`](./54-spiral-matrix/spiral-matrix.py) |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`jump-game.py`](./55-jump-game/jump-game.py) |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`merge-intervals.py`](./56-merge-intervals/merge-intervals.py) |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`insert-interval.py`](./57-insert-interval/insert-interval.py) |
| 58 | [Length of Last Word](https://leetcode.com/problems/length-of-last-word) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`length-of-last-word.py`](./58-length-of-last-word/length-of-last-word.py) |
| 59 | [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`spiral-matrix-ii.py`](./59-spiral-matrix-ii/spiral-matrix-ii.py) |
| 60 | [Permutation Sequence](https://leetcode.com/problems/permutation-sequence) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`permutation-sequence.py`](./60-permutation-sequence/permutation-sequence.py) |
| 61 | [Rotate List](https://leetcode.com/problems/rotate-list) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`rotate-list.py`](./61-rotate-list/rotate-list.py) |
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`unique-paths.py`](./62-unique-paths/unique-paths.py) |
| 63 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`unique-paths-ii.py`](./63-unique-paths-ii/unique-paths-ii.py) |
| 64 | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`minimum-path-sum.py`](./64-minimum-path-sum/minimum-path-sum.py) |
| 65 | [Valid Number](https://leetcode.com/problems/valid-number) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`valid-number.py`](./65-valid-number/valid-number.py) |
| 66 | [Plus One](https://leetcode.com/problems/plus-one) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`plus-one.py`](./66-plus-one/plus-one.py) |
| 67 | [Add Binary](https://leetcode.com/problems/add-binary) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`add-binary.py`](./67-add-binary/add-binary.py) |
| 68 | [Text Justification](https://leetcode.com/problems/text-justification) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`text-justification.py`](./68-text-justification/text-justification.py) |
| 69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`sqrtx.py`](./69-sqrtx/sqrtx.py) |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`climbing-stairs.py`](./70-climbing-stairs/climbing-stairs.py) |
| 71 | [Simplify Path](https://leetcode.com/problems/simplify-path) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`simplify-path.py`](./71-simplify-path/simplify-path.py) |
| 72 | [Edit Distance](https://leetcode.com/problems/edit-distance) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`edit-distance.py`](./72-edit-distance/edit-distance.py) |
| 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`set-matrix-zeroes.py`](./73-set-matrix-zeroes/set-matrix-zeroes.py) |
| 74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`search-a-2d-matrix.py`](./74-search-a-2d-matrix/search-a-2d-matrix.py) |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`sort-colors.py`](./75-sort-colors/sort-colors.py) |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`minimum-window-substring.py`](./76-minimum-window-substring/minimum-window-substring.py) |
| 77 | [Combinations](https://leetcode.com/problems/combinations) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`combinations.py`](./77-combinations/combinations.py) |
| 78 | [Subsets](https://leetcode.com/problems/subsets) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`subsets.py`](./78-subsets/subsets.py) |
| 79 | [Word Search](https://leetcode.com/problems/word-search) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`word-search.py`](./79-word-search/word-search.py) |
| 80 | [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`remove-duplicates-from-sorted-array-ii.py`](./80-remove-duplicates-from-sorted-array-ii/remove-duplicates-from-sorted-array-ii.py) |
| 81 | [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`search-in-rotated-sorted-array-ii.py`](./81-search-in-rotated-sorted-array-ii/search-in-rotated-sorted-array-ii.py) |
| 82 | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`remove-duplicates-from-sorted-list-ii.py`](./82-remove-duplicates-from-sorted-list-ii/remove-duplicates-from-sorted-list-ii.py) |
| 83 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`remove-duplicates-from-sorted-list.py`](./83-remove-duplicates-from-sorted-list/remove-duplicates-from-sorted-list.py) |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`largest-rectangle-in-histogram.py`](./84-largest-rectangle-in-histogram/largest-rectangle-in-histogram.py) |
| 85 | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`maximal-rectangle.py`](./85-maximal-rectangle/maximal-rectangle.py) |
| 86 | [Partition List](https://leetcode.com/problems/partition-list) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`partition-list.py`](./86-partition-list/partition-list.py) |
| 87 | [Scramble String](https://leetcode.com/problems/scramble-string) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`scramble-string.py`](./87-scramble-string/scramble-string.py) |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`merge-sorted-array.py`](./88-merge-sorted-array/merge-sorted-array.py) |
| 89 | [Gray Code](https://leetcode.com/problems/gray-code) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`gray-code.py`](./89-gray-code/gray-code.py) |
| 90 | [Subsets II](https://leetcode.com/problems/subsets-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`subsets-ii.py`](./90-subsets-ii/subsets-ii.py) |
| 91 | [Decode Ways](https://leetcode.com/problems/decode-ways) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`decode-ways.py`](./91-decode-ways/decode-ways.py) |
| 92 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`reverse-linked-list-ii.py`](./92-reverse-linked-list-ii/reverse-linked-list-ii.py) |
| 93 | [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`restore-ip-addresses.py`](./93-restore-ip-addresses/restore-ip-addresses.py) |
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`binary-tree-inorder-traversal.py`](./94-binary-tree-inorder-traversal/binary-tree-inorder-traversal.py) |
| 95 | [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`unique-binary-search-trees-ii.py`](./95-unique-binary-search-trees-ii/unique-binary-search-trees-ii.py) |
| 96 | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`unique-binary-search-trees.py`](./96-unique-binary-search-trees/unique-binary-search-trees.py) |
| 97 | [Interleaving String](https://leetcode.com/problems/interleaving-string) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`interleaving-string.py`](./97-interleaving-string/interleaving-string.py) |
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`validate-binary-search-tree.py`](./98-validate-binary-search-tree/validate-binary-search-tree.py) |
| 99 | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`recover-binary-search-tree.py`](./99-recover-binary-search-tree/recover-binary-search-tree.py) |
| 100 | [Same Tree](https://leetcode.com/problems/same-tree) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`same-tree.py`](./100-same-tree/same-tree.py) |
| 101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`symmetric-tree.py`](./101-symmetric-tree/symmetric-tree.py) |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`binary-tree-level-order-traversal.py`](./102-binary-tree-level-order-traversal/binary-tree-level-order-traversal.py) |
| 103 | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`binary-tree-zigzag-level-order-traversal.py`](./103-binary-tree-zigzag-level-order-traversal/binary-tree-zigzag-level-order-traversal.py) |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`maximum-depth-of-binary-tree.py`](./104-maximum-depth-of-binary-tree/maximum-depth-of-binary-tree.py) |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`construct-binary-tree-from-preorder-and-inorder-traversal.py`](./105-construct-binary-tree-from-preorder-and-inorder-traversal/construct-binary-tree-from-preorder-and-inorder-traversal.py) |
| 106 | [Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`construct-binary-tree-from-inorder-and-postorder-traversal.py`](./106-construct-binary-tree-from-inorder-and-postorder-traversal/construct-binary-tree-from-inorder-and-postorder-traversal.py) |
| 107 | [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`binary-tree-level-order-traversal-ii.py`](./107-binary-tree-level-order-traversal-ii/binary-tree-level-order-traversal-ii.py) |
| 108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`convert-sorted-array-to-binary-search-tree.py`](./108-convert-sorted-array-to-binary-search-tree/convert-sorted-array-to-binary-search-tree.py) |
| 109 | [Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`convert-sorted-list-to-binary-search-tree.py`](./109-convert-sorted-list-to-binary-search-tree/convert-sorted-list-to-binary-search-tree.py) |
| 110 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`balanced-binary-tree.py`](./110-balanced-binary-tree/balanced-binary-tree.py) |
| 111 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`minimum-depth-of-binary-tree.py`](./111-minimum-depth-of-binary-tree/minimum-depth-of-binary-tree.py) |
| 112 | [Path Sum](https://leetcode.com/problems/path-sum) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`path-sum.py`](./112-path-sum/path-sum.py) |
| 113 | [Path Sum II](https://leetcode.com/problems/path-sum-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`path-sum-ii.py`](./113-path-sum-ii/path-sum-ii.py) |
| 114 | [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`flatten-binary-tree-to-linked-list.py`](./114-flatten-binary-tree-to-linked-list/flatten-binary-tree-to-linked-list.py) |
| 115 | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`distinct-subsequences.py`](./115-distinct-subsequences/distinct-subsequences.py) |
| 116 | [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`populating-next-right-pointers-in-each-node.py`](./116-populating-next-right-pointers-in-each-node/populating-next-right-pointers-in-each-node.py) |
| 117 | [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`populating-next-right-pointers-in-each-node-ii.py`](./117-populating-next-right-pointers-in-each-node-ii/populating-next-right-pointers-in-each-node-ii.py) |
| 118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`pascals-triangle.py`](./118-pascals-triangle/pascals-triangle.py) |
| 119 | [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`pascals-triangle-ii.py`](./119-pascals-triangle-ii/pascals-triangle-ii.py) |
| 120 | [Triangle](https://leetcode.com/problems/triangle) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`triangle.py`](./120-triangle/triangle.py) |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`best-time-to-buy-and-sell-stock.py`](./121-best-time-to-buy-and-sell-stock/best-time-to-buy-and-sell-stock.py) |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`best-time-to-buy-and-sell-stock-ii.py`](./122-best-time-to-buy-and-sell-stock-ii/best-time-to-buy-and-sell-stock-ii.py) |
| 123 | [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`best-time-to-buy-and-sell-stock-iii.py`](./123-best-time-to-buy-and-sell-stock-iii/best-time-to-buy-and-sell-stock-iii.py) |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`binary-tree-maximum-path-sum.py`](./124-binary-tree-maximum-path-sum/binary-tree-maximum-path-sum.py) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`valid-palindrome.py`](./125-valid-palindrome/valid-palindrome.py) |
| 127 | [Word Ladder](https://leetcode.com/problems/word-ladder) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`word-ladder.py`](./127-word-ladder/word-ladder.py) |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`longest-consecutive-sequence.py`](./128-longest-consecutive-sequence/longest-consecutive-sequence.py) |
| 129 | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`sum-root-to-leaf-numbers.py`](./129-sum-root-to-leaf-numbers/sum-root-to-leaf-numbers.py) |
| 130 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`surrounded-regions.py`](./130-surrounded-regions/surrounded-regions.py) |
| 131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`palindrome-partitioning.py`](./131-palindrome-partitioning/palindrome-partitioning.py) |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`clone-graph.py`](./133-clone-graph/clone-graph.py) |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`gas-station.py`](./134-gas-station/gas-station.py) |
| 135 | [Candy](https://leetcode.com/problems/candy) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`candy.py`](./135-candy/candy.py) |
| 136 | [Single Number](https://leetcode.com/problems/single-number) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`single-number.py`](./136-single-number/single-number.py) |
| 137 | [Single Number II](https://leetcode.com/problems/single-number-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`single-number-ii.py`](./137-single-number-ii/single-number-ii.py) |
| 138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`copy-list-with-random-pointer.py`](./138-copy-list-with-random-pointer/copy-list-with-random-pointer.py) |
| 139 | [Word Break](https://leetcode.com/problems/word-break) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`word-break.py`](./139-word-break/word-break.py) |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`linked-list-cycle.py`](./141-linked-list-cycle/linked-list-cycle.py) |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`linked-list-cycle-ii.py`](./142-linked-list-cycle-ii/linked-list-cycle-ii.py) |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`reorder-list.py`](./143-reorder-list/reorder-list.py) |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`lru-cache.py`](./146-lru-cache/lru-cache.py) |
| 148 | [Sort List](https://leetcode.com/problems/sort-list) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`sort-list.py`](./148-sort-list/sort-list.py) |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`evaluate-reverse-polish-notation.py`](./150-evaluate-reverse-polish-notation/evaluate-reverse-polish-notation.py) |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`maximum-product-subarray.py`](./152-maximum-product-subarray/maximum-product-subarray.py) |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`find-minimum-in-rotated-sorted-array.py`](./153-find-minimum-in-rotated-sorted-array/find-minimum-in-rotated-sorted-array.py) |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`min-stack.py`](./155-min-stack/min-stack.py) |
| 198 | [House Robber](https://leetcode.com/problems/house-robber) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`house-robber.py`](./198-house-robber/house-robber.py) |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`number-of-islands.py`](./200-number-of-islands/number-of-islands.py) |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`reverse-linked-list.py`](./206-reverse-linked-list/reverse-linked-list.py) |
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`find-the-duplicate-number.py`](./287-find-the-duplicate-number/find-the-duplicate-number.py) |
| 628 | [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`maximum-product-of-three-numbers.py`](./628-maximum-product-of-three-numbers/maximum-product-of-three-numbers.py) |
| 678 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`valid-parenthesis-string.py`](./678-valid-parenthesis-string/valid-parenthesis-string.py) |
| 864 | [Image Overlap](https://leetcode.com/problems/image-overlap) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`image-overlap.py`](./864-image-overlap/image-overlap.py) |
| 866 | [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`rectangle-overlap.py`](./866-rectangle-overlap/rectangle-overlap.py) |
| 909 | [Stone Game](https://leetcode.com/problems/stone-game) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`stone-game.py`](./909-stone-game/stone-game.py) |
| 977 | [Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`distinct-subsequences-ii.py`](./977-distinct-subsequences-ii/distinct-subsequences-ii.py) |
| 1159 | [Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`smallest-subsequence-of-distinct-characters.py`](./1159-smallest-subsequence-of-distinct-characters/smallest-subsequence-of-distinct-characters.py) |
| 1188 | [Brace Expansion II](https://leetcode.com/problems/brace-expansion-ii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`brace-expansion-ii.py`](./1188-brace-expansion-ii/brace-expansion-ii.py) |
| 1208 | [Maximum Nesting Depth of Two Valid Parentheses Strings](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`maximum-nesting-depth-of-two-valid-parentheses-strings.py`](./1208-maximum-nesting-depth-of-two-valid-parentheses-strings/maximum-nesting-depth-of-two-valid-parentheses-strings.py) |
| 1212 | [Sequential Digits](https://leetcode.com/problems/sequential-digits) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`sequential-digits.py`](./1212-sequential-digits/sequential-digits.py) |
| 1240 | [Stone Game II](https://leetcode.com/problems/stone-game-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`stone-game-ii.py`](./1240-stone-game-ii/stone-game-ii.py) |
| 1256 | [Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`rank-transform-of-an-array.py`](./1256-rank-transform-of-an-array/rank-transform-of-an-array.py) |
| 1298 | [Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`reverse-substrings-between-each-pair-of-parentheses.py`](./1298-reverse-substrings-between-each-pair-of-parentheses/reverse-substrings-between-each-pair-of-parentheses.py) |
| 1386 | [Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`shift-2d-grid.py`](./1386-shift-2d-grid/shift-2d-grid.py) |
| 1487 | [Cinema Seat Allocation](https://leetcode.com/problems/cinema-seat-allocation) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`cinema-seat-allocation.py`](./1487-cinema-seat-allocation/cinema-seat-allocation.py) |
| 1501 | [Circle and Rectangle Overlapping](https://leetcode.com/problems/circle-and-rectangle-overlapping) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`circle-and-rectangle-overlapping.py`](./1501-circle-and-rectangle-overlapping/circle-and-rectangle-overlapping.py) |
| 1522 | [Stone Game III](https://leetcode.com/problems/stone-game-iii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`stone-game-iii.py`](./1522-stone-game-iii/stone-game-iii.py) |
| 1573 | [Find Two Non-overlapping Sub-arrays Each With Target Sum](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`find-two-non-overlapping-sub-arrays-each-with-target-sum.py`](./1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/find-two-non-overlapping-sub-arrays-each-with-target-sum.py) |
| 1574 | [Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`maximum-product-of-two-elements-in-an-array.py`](./1574-maximum-product-of-two-elements-in-an-array/maximum-product-of-two-elements-in-an-array.py) |
| 1617 | [Stone Game IV](https://leetcode.com/problems/stone-game-iv) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`stone-game-iv.py`](./1617-stone-game-iv/stone-game-iv.py) |
| 1644 | [Maximum Number of Non-Overlapping Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`maximum-number-of-non-overlapping-substrings.py`](./1644-maximum-number-of-non-overlapping-substrings/maximum-number-of-non-overlapping-substrings.py) |
| 1685 | [Stone Game V](https://leetcode.com/problems/stone-game-v) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`stone-game-v.py`](./1685-stone-game-v/stone-game-v.py) |
| 1725 | [Number of Sets of K Non-Overlapping Line Segments](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`number-of-sets-of-k-non-overlapping-line-segments.py`](./1725-number-of-sets-of-k-non-overlapping-line-segments/number-of-sets-of-k-non-overlapping-line-segments.py) |
| 1737 | [Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`maximum-nesting-depth-of-the-parentheses.py`](./1737-maximum-nesting-depth-of-the-parentheses/maximum-nesting-depth-of-the-parentheses.py) |
| 1776 | [Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`minimum-operations-to-reduce-x-to-zero.py`](./1776-minimum-operations-to-reduce-x-to-zero/minimum-operations-to-reduce-x-to-zero.py) |
| 1934 | [Evaluate the Bracket Pairs of a String](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`evaluate-the-bracket-pairs-of-a-string.py`](./1934-evaluate-the-bracket-pairs-of-a-string/evaluate-the-bracket-pairs-of-a-string.py) |
| 2002 | [Stone Game VIII](https://leetcode.com/problems/stone-game-viii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`stone-game-viii.py`](./2002-stone-game-viii/stone-game-viii.py) |
| 2039 | [Sum Game](https://leetcode.com/problems/sum-game) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`sum-game.py`](./2039-sum-game/sum-game.py) |
| 2106 | [Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`find-greatest-common-divisor-of-array.py`](./2106-find-greatest-common-divisor-of-array/find-greatest-common-divisor-of-array.py) |
| 2156 | [Stone Game IX](https://leetcode.com/problems/stone-game-ix) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`stone-game-ix.py`](./2156-stone-game-ix/stone-game-ix.py) |
| 2182 | [Find the Minimum and Maximum Number of Nodes Between Critical Points](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`find-the-minimum-and-maximum-number-of-nodes-between-critical-points.py`](./2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/find-the-minimum-and-maximum-number-of-nodes-between-critical-points.py) |
| 2212 | [Removing Minimum and Maximum From Array](https://leetcode.com/problems/removing-minimum-and-maximum-from-array) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`removing-minimum-and-maximum-from-array.py`](./2212-removing-minimum-and-maximum-from-array/removing-minimum-and-maximum-from-array.py) |
| 2319 | [Longest Substring of One Repeating Character](https://leetcode.com/problems/longest-substring-of-one-repeating-character) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`longest-substring-of-one-repeating-character.py`](./2319-longest-substring-of-one-repeating-character/longest-substring-of-one-repeating-character.py) |
| 2347 | [Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`count-nodes-equal-to-average-of-subtree.py`](./2347-count-nodes-equal-to-average-of-subtree/count-nodes-equal-to-average-of-subtree.py) |
| 2349 | [Check if There Is a Valid Parentheses String Path](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`check-if-there-is-a-valid-parentheses-string-path.py`](./2349-check-if-there-is-a-valid-parentheses-string-path/check-if-there-is-a-valid-parentheses-string-path.py) |
| 2559 | [Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`maximum-number-of-non-overlapping-palindrome-substrings.py`](./2559-maximum-number-of-non-overlapping-palindrome-substrings/maximum-number-of-non-overlapping-palindrome-substrings.py) |
| 2582 | [Minimum Score of a Path Between Two Cities](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`minimum-score-of-a-path-between-two-cities.py`](./2582-minimum-score-of-a-path-between-two-cities/minimum-score-of-a-path-between-two-cities.py) |
| 2793 | [Count the Number of Complete Components](https://leetcode.com/problems/count-the-number-of-complete-components) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`count-the-number-of-complete-components.py`](./2793-count-the-number-of-complete-components/count-the-number-of-complete-components.py) |
| 2914 | [Find the Safest Path in a Grid](https://leetcode.com/problems/find-the-safest-path-in-a-grid) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`find-the-safest-path-in-a-grid.py`](./2914-find-the-safest-path-in-a-grid/find-the-safest-path-in-a-grid.py) |
| 3150 | [Shortest and Lexicographically Smallest Beautiful String](https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`shortest-and-lexicographically-smallest-beautiful-string.py`](./3150-shortest-and-lexicographically-smallest-beautiful-string/shortest-and-lexicographically-smallest-beautiful-string.py) |
| 3219 | [Make Lexicographically Smallest Array by Swapping Elements](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`make-lexicographically-smallest-array-by-swapping-elements.py`](./3219-make-lexicographically-smallest-array-by-swapping-elements/make-lexicographically-smallest-array-by-swapping-elements.py) |
| 3225 | [Length of Longest Subarray With at Most K Frequency](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`length-of-longest-subarray-with-at-most-k-frequency.py`](./3225-length-of-longest-subarray-with-at-most-k-frequency/length-of-longest-subarray-with-at-most-k-frequency.py) |
| 3236 | [Smallest Missing Integer Greater Than Sequential Prefix Sum](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`smallest-missing-integer-greater-than-sequential-prefix-sum.py`](./3236-smallest-missing-integer-greater-than-sequential-prefix-sum/smallest-missing-integer-greater-than-sequential-prefix-sum.py) |
| 3275 | [Minimum Number of Pushes to Type Word I](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`minimum-number-of-pushes-to-type-word-i.py`](./3275-minimum-number-of-pushes-to-type-word-i/minimum-number-of-pushes-to-type-word-i.py) |
| 3276 | [Minimum Number of Pushes to Type Word II](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`minimum-number-of-pushes-to-type-word-ii.py`](./3276-minimum-number-of-pushes-to-type-word-ii/minimum-number-of-pushes-to-type-word-ii.py) |
| 3349 | [Maximum Length Substring With Two Occurrences](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`maximum-length-substring-with-two-occurrences.py`](./3349-maximum-length-substring-with-two-occurrences/maximum-length-substring-with-two-occurrences.py) |
| 3375 | [Kth Smallest Amount With Single Denomination Combination](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`kth-smallest-amount-with-single-denomination-combination.py`](./3375-kth-smallest-amount-with-single-denomination-combination/kth-smallest-amount-with-single-denomination-combination.py) |
| 3558 | [Find a Safe Walk Through a Grid](https://leetcode.com/problems/find-a-safe-walk-through-a-grid) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`find-a-safe-walk-through-a-grid.py`](./3558-find-a-safe-walk-through-a-grid/find-a-safe-walk-through-a-grid.py) |
| 3561 | [Remove Methods From Project](https://leetcode.com/problems/remove-methods-from-project) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`remove-methods-from-project.py`](./3561-remove-methods-from-project/remove-methods-from-project.py) |
| 3562 | [Maximum Score of Non-overlapping Intervals](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`maximum-score-of-non-overlapping-intervals.py`](./3562-maximum-score-of-non-overlapping-intervals/maximum-score-of-non-overlapping-intervals.py) |
| 3583 | [Sorted GCD Pair Queries](https://leetcode.com/problems/sorted-gcd-pair-queries) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`sorted-gcd-pair-queries.py`](./3583-sorted-gcd-pair-queries/sorted-gcd-pair-queries.py) |
| 3584 | [Find the Lexicographically Smallest Valid Sequence](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`find-the-lexicographically-smallest-valid-sequence.py`](./3584-find-the-lexicographically-smallest-valid-sequence/find-the-lexicographically-smallest-valid-sequence.py) |
| 3608 | [Find the Number of Subsequences With Equal GCD](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`find-the-number-of-subsequences-with-equal-gcd.py`](./3608-find-the-number-of-subsequences-with-equal-gcd/find-the-number-of-subsequences-with-equal-gcd.py) |
| 3626 | [Smallest Divisible Digit Product I](https://leetcode.com/problems/smallest-divisible-digit-product-i) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`smallest-divisible-digit-product-i.py`](./3626-smallest-divisible-digit-product-i/smallest-divisible-digit-product-i.py) |
| 3635 | [Smallest Divisible Digit Product II](https://leetcode.com/problems/smallest-divisible-digit-product-ii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`smallest-divisible-digit-product-ii.py`](./3635-smallest-divisible-digit-product-ii/smallest-divisible-digit-product-ii.py) |
| 3705 | [Find the Largest Almost Missing Integer](https://leetcode.com/problems/find-the-largest-almost-missing-integer) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`find-the-largest-almost-missing-integer.py`](./3705-find-the-largest-almost-missing-integer/find-the-largest-almost-missing-integer.py) |
| 3799 | [Unique 3-Digit Even Numbers](https://leetcode.com/problems/unique-3-digit-even-numbers) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`unique-3-digit-even-numbers.py`](./3799-unique-3-digit-even-numbers/unique-3-digit-even-numbers.py) |
| 3804 | [Maximize Active Section with Trade II](https://leetcode.com/problems/maximize-active-section-with-trade-ii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`maximize-active-section-with-trade-ii.py`](./3804-maximize-active-section-with-trade-ii/maximize-active-section-with-trade-ii.py) |
| 3805 | [Maximize Active Section with Trade I](https://leetcode.com/problems/maximize-active-section-with-trade-i) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`maximize-active-section-with-trade-i.py`](./3805-maximize-active-section-with-trade-i/maximize-active-section-with-trade-i.py) |
| 3811 | [Reverse Degree of a String](https://leetcode.com/problems/reverse-degree-of-a-string) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`reverse-degree-of-a-string.py`](./3811-reverse-degree-of-a-string/reverse-degree-of-a-string.py) |
| 3812 | [Smallest Palindromic Rearrangement I](https://leetcode.com/problems/smallest-palindromic-rearrangement-i) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`smallest-palindromic-rearrangement-i.py`](./3812-smallest-palindromic-rearrangement-i/smallest-palindromic-rearrangement-i.py) |
| 3813 | [Smallest Palindromic Rearrangement II](https://leetcode.com/problems/smallest-palindromic-rearrangement-ii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`smallest-palindromic-rearrangement-ii.py`](./3813-smallest-palindromic-rearrangement-ii/smallest-palindromic-rearrangement-ii.py) |
| 3820 | [Number of Unique XOR Triplets II](https://leetcode.com/problems/number-of-unique-xor-triplets-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`number-of-unique-xor-triplets-ii.py`](./3820-number-of-unique-xor-triplets-ii/number-of-unique-xor-triplets-ii.py) |
| 3824 | [Number of Unique XOR Triplets I](https://leetcode.com/problems/number-of-unique-xor-triplets-i) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`number-of-unique-xor-triplets-i.py`](./3824-number-of-unique-xor-triplets-i/number-of-unique-xor-triplets-i.py) |
| 3831 | [Find X Value of Array I](https://leetcode.com/problems/find-x-value-of-array-i) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`find-x-value-of-array-i.py`](./3831-find-x-value-of-array-i/find-x-value-of-array-i.py) |
| 3838 | [Path Existence Queries in a Graph I](https://leetcode.com/problems/path-existence-queries-in-a-graph-i) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`path-existence-queries-in-a-graph-i.py`](./3838-path-existence-queries-in-a-graph-i/path-existence-queries-in-a-graph-i.py) |
| 3840 | [Find X Value of Array II](https://leetcode.com/problems/find-x-value-of-array-ii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`find-x-value-of-array-ii.py`](./3840-find-x-value-of-array-ii/find-x-value-of-array-ii.py) |
| 3852 | [Path Existence Queries in a Graph II](https://leetcode.com/problems/path-existence-queries-in-a-graph-ii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`path-existence-queries-in-a-graph-ii.py`](./3852-path-existence-queries-in-a-graph-ii/path-existence-queries-in-a-graph-ii.py) |
| 3859 | [Maximum Product of Two Digits](https://leetcode.com/problems/maximum-product-of-two-digits) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`maximum-product-of-two-digits.py`](./3859-maximum-product-of-two-digits/maximum-product-of-two-digits.py) |
| 3869 | [Smallest Index With Digit Sum Equal to Index](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`smallest-index-with-digit-sum-equal-to-index.py`](./3869-smallest-index-with-digit-sum-equal-to-index/smallest-index-with-digit-sum-equal-to-index.py) |
| 3870 | [Minimum Moves to Clean the Classroom](https://leetcode.com/problems/minimum-moves-to-clean-the-classroom) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`minimum-moves-to-clean-the-classroom.py`](./3870-minimum-moves-to-clean-the-classroom/minimum-moves-to-clean-the-classroom.py) |
| 3918 | [Check Divisibility by Digit Sum and Product](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`check-divisibility-by-digit-sum-and-product.py`](./3918-check-divisibility-by-digit-sum-and-product/check-divisibility-by-digit-sum-and-product.py) |
| 3995 | [GCD of Odd and Even Sums](https://leetcode.com/problems/gcd-of-odd-and-even-sums) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`gcd-of-odd-and-even-sums.py`](./3995-gcd-of-odd-and-even-sums/gcd-of-odd-and-even-sums.py) |
| 4020 | [Lexicographically Smallest Permutation Greater Than Target](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`lexicographically-smallest-permutation-greater-than-target.py`](./4020-lexicographically-smallest-permutation-greater-than-target/lexicographically-smallest-permutation-greater-than-target.py) |
| 4033 | [Longest Subsequence With Non-Zero Bitwise XOR](https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`longest-subsequence-with-non-zero-bitwise-xor.py`](./4033-longest-subsequence-with-non-zero-bitwise-xor/longest-subsequence-with-non-zero-bitwise-xor.py) |
| 4037 | [Lexicographically Smallest Palindromic Permutation Greater Than Target](https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`lexicographically-smallest-palindromic-permutation-greater-than-target.py`](./4037-lexicographically-smallest-palindromic-permutation-greater-than-target/lexicographically-smallest-palindromic-permutation-greater-than-target.py) |
| 4080 | [Smallest Missing Multiple of K](https://leetcode.com/problems/smallest-missing-multiple-of-k) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`smallest-missing-multiple-of-k.py`](./4080-smallest-missing-multiple-of-k/smallest-missing-multiple-of-k.py) |
| 4107 | [Find Missing Elements](https://leetcode.com/problems/find-missing-elements) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`find-missing-elements.py`](./4107-find-missing-elements/find-missing-elements.py) |
| 4135 | [Concatenate Non-Zero Digits and Multiply by Sum I](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`concatenate-non-zero-digits-and-multiply-by-sum-i.py`](./4135-concatenate-non-zero-digits-and-multiply-by-sum-i/concatenate-non-zero-digits-and-multiply-by-sum-i.py) |
| 4136 | [Concatenate Non-Zero Digits and Multiply by Sum II](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`concatenate-non-zero-digits-and-multiply-by-sum-ii.py`](./4136-concatenate-non-zero-digits-and-multiply-by-sum-ii/concatenate-non-zero-digits-and-multiply-by-sum-ii.py) |
| 4203 | [Count of Unfinished Tasks After Each Shift](https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`count-of-unfinished-tasks-after-each-shift.py`](./4203-count-of-unfinished-tasks-after-each-shift/count-of-unfinished-tasks-after-each-shift.py) |
| 4242 | [Sum of GCD of Formed Pairs](https://leetcode.com/problems/sum-of-gcd-of-formed-pairs) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`sum-of-gcd-of-formed-pairs.py`](./4242-sum-of-gcd-of-formed-pairs/sum-of-gcd-of-formed-pairs.py) |
| 4245 | [Count Commas in Range](https://leetcode.com/problems/count-commas-in-range) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`count-commas-in-range.py`](./4245-count-commas-in-range/count-commas-in-range.py) |
| 4248 | [Count Commas in Range II](https://leetcode.com/problems/count-commas-in-range-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`count-commas-in-range-ii.py`](./4248-count-commas-in-range-ii/count-commas-in-range-ii.py) |
| 4256 | [Construct Uniform Parity Array I](https://leetcode.com/problems/construct-uniform-parity-array-i) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`construct-uniform-parity-array-i.py`](./4256-construct-uniform-parity-array-i/construct-uniform-parity-array-i.py) |
| 4258 | [Construct Uniform Parity Array II](https://leetcode.com/problems/construct-uniform-parity-array-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`construct-uniform-parity-array-ii.py`](./4258-construct-uniform-parity-array-ii/construct-uniform-parity-array-ii.py) |
| 4284 | [Smallest Stable Index I](https://leetcode.com/problems/smallest-stable-index-i) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`smallest-stable-index-i.py`](./4284-smallest-stable-index-i/smallest-stable-index-i.py) |
| 4285 | [Smallest Stable Index II](https://leetcode.com/problems/smallest-stable-index-ii) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`smallest-stable-index-ii.py`](./4285-smallest-stable-index-ii/smallest-stable-index-ii.py) |
| 4323 | [Count Subarrays With Even Odd Ratio I](https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i) | ![Medium](https://img.shields.io/badge/Medium-orange) | Python 3.12 | [`count-subarrays-with-even-odd-ratio-i.py`](./4323-count-subarrays-with-even-odd-ratio-i/count-subarrays-with-even-odd-ratio-i.py) |
| 4324 | [Count Subarrays With Even Odd Ratio II](https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii) | ![Hard](https://img.shields.io/badge/Hard-red) | Python 3.12 | [`count-subarrays-with-even-odd-ratio-ii.py`](./4324-count-subarrays-with-even-odd-ratio-ii/count-subarrays-with-even-odd-ratio-ii.py) |
| 4371 | [Maximize Pair Strength Using GCD](https://leetcode.com/problems/maximize-pair-strength-using-gcd) | ![Easy](https://img.shields.io/badge/Easy-brightgreen) | Python 3.12 | [`maximize-pair-strength-using-gcd.py`](./4371-maximize-pair-strength-using-gcd/maximize-pair-strength-using-gcd.py) |

---

## 🧪 Local Execution & Testing Guide

### Prerequisites
- Python 3.10+ (Python 3.12 recommended)

### Run Any Solution Locally:
```bash
# Clone the repository
git clone https://github.com/preyal2/daily-leetcode.git
cd daily-leetcode

# Example 1: Run LeetCode 124 Binary Tree Maximum Path Sum
python -c "
from importlib import import_module
mod = import_module('124-binary-tree-maximum-path-sum.binary-tree-maximum-path-sum')
sol = mod.Solution()
TreeNode = mod.TreeNode
root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print('Max Path Sum:', sol.maxPathSum(root))
"

# Example 2: Run LeetCode 139 Word Break
python -c "
from importlib import import_module
mod = import_module('139-word-break.word-break')
sol = mod.Solution()
print('Word Break:', sol.wordBreak('leetcode', ['leet', 'code']))
"

# Example 3: Run LeetCode 155 Min Stack
python -c "
from importlib import import_module
mod = import_module('155-min-stack.min-stack')
MinStack = mod.MinStack
st = MinStack()
st.push(-2)
st.push(0)
st.push(-3)
print('Min Stack getMin():', st.getMin())
st.pop()
print('Top:', st.top())
print('Min Stack getMin():', st.getMin())
"
```

---

## 🤝 Contributing

Contributions, optimizations, and multi-language ports (Java, C++, TypeScript, Go) are welcome! Please refer to the [**`CONTRIBUTING.md`**](./CONTRIBUTING.md) guide for PR instructions.

---

## 👨‍💻 Author

**Modi Preyal**
- **GitHub**: [@preyal2](https://github.com/preyal2)
- **Email**: [modipreyal@gmail.com](mailto:modipreyal@gmail.com)
- **LinkedIn**: [preyalmodi](https://www.linkedin.com/in/preyalmodi/)
- **Portfolio**: [https://preyal1portfolio.netlify.app/](https://preyal1portfolio.netlify.app/)
