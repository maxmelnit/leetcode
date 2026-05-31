class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Strs with differing lens can't be anagrams
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        str_len = len(s)

        # Construct freq map -> s_map, t_map = {r: 2, a: 2, ...}
        for i in range(str_len):
            if not s[i] in s_map:
                s_map[s[i]] = 1
            else:
                s_map[s[i]] += 1

            if not t[i] in t_map:
                t_map[t[i]] = 1
            else:
                t_map[t[i]] += 1


        print(s_map, t_map)

        for key in s_map.keys():

            if key not in t_map:
                return False
            else:
                if s_map[key] != t_map[key]:
                    return False
        
        return True



            