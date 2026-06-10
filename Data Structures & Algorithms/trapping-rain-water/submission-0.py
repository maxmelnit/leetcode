class Solution:
    def trap(self, height: List[int]) -> int:
        
        h = len(height)
        l_best = [0] * h
        r_best = [0] * h
        trapped = [0] * h

        l_max = 0
        r_max = 0

        for i in range(1, h):
            l_best[i] = max(l_max, height[i - 1])
            l_max = l_best[i]

        for i in range(h - 2, -1, -1):
            r_best[i] = max(r_max, height[i + 1])
            r_max = r_best[i]

        for i in range(h):
            trapped[i] = max(min(l_best[i], r_best[i]) - height[i], 0)

        return sum(trapped)

        