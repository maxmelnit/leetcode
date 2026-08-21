class Solution:

    def encode(self, strs: List[str]) -> str:
        
        string = ""
        for s in strs:
            string += str(len(s)) + '#' + s
            
        return string



    def decode(self, s: str) -> List[str]:

        str_list = []

        "5#Hello5#World"

        i = 0
        while i < len(s):
            string = ""
            str_len = ""

            while s[i] != '#':
                str_len += s[i]
                i += 1
            i += 1 # Have to move past the tag too

            for j in range(int(str_len)):
                string += s[i]
                i += 1

            str_list.append(string)
            

        return str_list