class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
    
        res = []

        for i, interval in enumerate(intervals):
            intervals_x = interval[0]
            intervals_y = interval[1]

            if newInterval[1] < intervals_x:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res

            elif newInterval[0] > intervals_y:
                res.append(interval)

            else: # Overlapping case
                newInterval = [min(intervals_x, newInterval[0]), max(intervals_y, newInterval[1])]

        res.append(newInterval)
            

        return res