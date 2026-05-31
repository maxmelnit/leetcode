class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        freq_map = {}
        
        # Create a frequency chart of each number w/ a hashmap -> O(n)
        for i in range(len(nums)):
            if not nums[i] in freq_map:
                freq_map[nums[i]] = 1
            else:
                freq_map[nums[i]] += 1


        for key in freq_map.keys(): # O(n)
            if freq_map[key] > 1:
                return True
        
        return False