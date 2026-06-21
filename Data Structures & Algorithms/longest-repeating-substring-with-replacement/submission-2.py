from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        best = 0
        l = 0
        r = 0
        freq_map = defaultdict(int)

        while r < len(s):

            freq_map[s[r]] += 1
            most_freq = 0

            for v in freq_map.values():
                if v > most_freq:
                    most_freq = v
            
            if (r - l + 1) - most_freq <= k:
                best = r - l + 1
            else:
                freq_map[s[l]] -= 1
                l += 1

            r += 1

        return best


            
