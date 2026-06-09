class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        best = 0
        l = 0
        r = len(heights) - 1

        while l < r:

            area = min(heights[l], heights[r]) * (r - l)
            if area > best:
                best = area

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
                l += 1

        return best
                
                

        