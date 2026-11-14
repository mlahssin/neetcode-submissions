from collections import deque
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        Max_surface = 0
        n = len(heights)

        right = [n - 1] * n
        left = [0] * n

        stack = deque()

        # Find left boundaries
        for index, height in enumerate(heights):

            while stack and heights[stack[-1]] >= height:
                stack.pop()

            if stack:
                left[index] = stack[-1] + 1

            stack.append(index)

        stack = []

        # Find right boundaries
        for index in range(n - 1, -1, -1):

            while stack and heights[stack[-1]] >= heights[index]:
                stack.pop()

            if stack:
                right[index] = stack[-1] - 1

            stack.append(index)

        # Calculate maximum rectangle area
        for index in range(n):

            width = right[index] - left[index] + 1

            Max_surface = max(
                Max_surface,
                width * heights[index]
            )

        return Max_surface