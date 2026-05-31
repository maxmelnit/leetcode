from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            anagram_list[key].append(string)

        return list(anagram_list.values())