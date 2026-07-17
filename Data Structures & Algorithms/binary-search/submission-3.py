class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        

        while l <= r:
            mid = (l + r) // 2

            if target < nums[mid]:
                r = mid - 1 # Move right pointer all the way past mid
            elif target > nums[mid]:
                l = mid + 1 # Move left pointer all the way past mid
            else:
                return mid # If the target is the midpoint

        return -1 # The case where the number wasn't found at all







