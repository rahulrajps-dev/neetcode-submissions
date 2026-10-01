class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights) - 1
        container=0

        while left < right:
            if heights[left] < heights[right]:
                container=max(container,heights[left] * (right-left))
                left+=1
            elif heights[right] < heights[left]:
                container = max(container,heights[right] * (right - left))
                right-=1
            else:
                container = max(container,heights[right] * (right - left))
                right-=1
                left+=1
        return container


