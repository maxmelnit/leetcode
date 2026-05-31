class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Need to build hashmap to keep track of number indices

        index_map = {}

        for i in range(len(nums)):
            index_map[nums[i]] = i # {3: 0, 4: 1, 5: 2, ...}
        
        for i in range(len(nums)):
            lookup = target - nums[i] # Want to find the other number that gives target
    

            if lookup in nums: # O(1) lookup
                lookup_index = index_map[lookup] # O(1)
                if lookup_index != i:
                    return [i, lookup_index]

        return []
