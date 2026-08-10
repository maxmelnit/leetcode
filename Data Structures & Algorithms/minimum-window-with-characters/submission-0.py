import math
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Init left/right pointers, and track count of letters seen
        l = 0
        r = 0
        best_l = l
        best_r = r
        best = math.inf
        t_map = defaultdict(int)
        s_map = defaultdict(int)

        # Freq map of each char in t
        for char in t:
            t_map[char] += 1


        # Need len(t) chars to satisfy
        have = 0
        need = len(t_map)
        while r < len(s): 
            char = s[r]

            if char in t_map:
                s_map[char] += 1 # Count freq of each char as we go

                # Only increment once (don't want to increase have more than once for the same char)
                if s_map[char] == t_map[char]:
                    have += 1

            # When we have a valid window
            while have == need:
                if r - l + 1 < best:
                    best_l = l
                    best_r = r
                    best = r - l + 1


                left_char = s[l]

                if left_char in t_map: # Remove it from the s map
                    s_map[left_char] -= 1

                    if s_map[left_char] < t_map[left_char]:
                        have -= 1

                l += 1

            r += 1

        return s[best_l:best_r+1] if best != math.inf else ""
            

        

        

