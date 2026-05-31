import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # First, we need to make a hashmap to count the element freqs:
        freq_map = defaultdict(int) # Dict of integer values

        for i in range(len(nums)): # Count freq of each number. defaultdict defaults to 0 if DNE already
            freq_map[nums[i]] += 1
        # Now we have {1: 1, 2: 2, 3: 5}

        heap = [] # Min heap by default, negate to get max heap
        for key in freq_map.keys():
            heapq.heappush(heap, (-freq_map[key], key))

        out = []
        for i in range(k):
            out.append(heapq.heappop(heap)[1])

        return out

        




