class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Turn nums into a set
        num_set = set(nums)
        best = 0

        for num in num_set:

            # If that number doesn't have a left neighbour, it's the start of a sequence
            if num - 1 not in num_set:
                curr = 0
                # Now, count how far we can get from the start of the sequence
                # Don't have to reset, because future sequences would have to beat num + best anyways
                while num + curr in num_set:
                    curr += 1

                best = max(curr, best)

                

        return best