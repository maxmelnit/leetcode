from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        char_map = defaultdict(int)

        for i in range(len(s1)):
            char_map[s1[i]] += 1
        
        # Starting max/min index
        r = len(s1) - 1
        w = len(s1) - 1
        l = 0

        while r < len(s2):

            temp_char_map = defaultdict(int)

            while l < r + 1:
                temp_char_map[s2[l]] += 1
                l += 1
            
            if temp_char_map == char_map:
                return True

            r += 1
            l = r - w

        return False



       

