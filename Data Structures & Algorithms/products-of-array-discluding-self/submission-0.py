import copy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # In is [1, 2, 4, 6]
        # Pre-fill out with len num of 1's
        out = [1] * len(nums) 

        prev = 1
        for i in range(len(nums)):
            out[i] *= prev
            prev *= nums[i]
            

        prev = 1
        for i in range(len(nums) - 1, -1, -1): # Start stop step
            out[i] *= prev
            prev *= nums[i]

        return out


        


        


