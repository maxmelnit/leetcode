class Solution:
    def isValid(self, s: str) -> bool:
        
        char_map = {'}': '{', ']': '[', ')': '('}
        stack = []
        for b in s:
            if b not in char_map: # Open bracket
                stack.append(b)
            else: # Closing brachet
                if not stack:
                    return False
                popped = stack.pop()
                if popped != char_map[b]:
                    return False

        return True if not stack else False


                



