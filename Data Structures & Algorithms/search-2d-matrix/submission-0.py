class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Build out a single array and do binary search

        full_list = []
        for arr in matrix:
            for num in arr:
                full_list.append(num)

        l = 0
        r = len(full_list) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == full_list[mid]:
                return True
            elif target < full_list[mid]:
                r = mid - 1
            elif target > full_list[mid]:
                l = mid + 1

        return False