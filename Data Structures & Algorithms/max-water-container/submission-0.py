class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left= 0
        right = len(heights)-1
        max = 0
        while left < right:
            width = right - left
            if heights[left]<= heights[right]:
                size = heights[left]* width
                left +=1
            elif heights[right] < heights[left]:
                size = heights[right]* width
                right-=1
            if size > max:
                max = size
        return max
