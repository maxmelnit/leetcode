"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if len(intervals) == 1:
            return True
            
        intervals_list = []
        for i in intervals:
            intervals_list.append([i.start, i.end])

        intervals_list.sort()

        l = 0
        r = l + 1

        while r < len(intervals_list):
            
            i1x = intervals_list[l][0]
            i1y = intervals_list[l][1]
            i2x = intervals_list[r][0]
            i2y = intervals_list[r][1]

            if i1x < i2y and i1y > i2x:
                return False
            
            l += 1
            r += 1

        return True
