class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * len(matrix[0])
        ans = 0

        for row in matrix:
            for j in range(len(row)):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            cur = self.largestRectangleArea(heights)
            if cur > ans:
                ans = cur

        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(heights) + 1):
            h = heights[i] if i < len(heights) else 0

            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                area = height * (i - left)

                if area > ans:
                    ans = area

            stack.append(i)

        return ans