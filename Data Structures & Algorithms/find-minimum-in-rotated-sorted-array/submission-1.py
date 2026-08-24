class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        lo = 0
        hi = len(nums) - 1
        best = math.inf

        while lo <= hi:
            mid = (lo + hi) // 2
            best = min(best, nums[mid]) # Update the best if we find a smaller value than the current smallest

            if nums[mid] > nums[hi]: # Means a pivot is between mid and hi, so look there
                lo = mid + 1
            elif nums[mid] < nums[hi]: # Pivot isn't on the left, so the smallest num is to the right
                hi = mid - 1
            else:
                break

        return best

            

