'''
Meeting rooms.
Given an array of start and end times [[s1,e1],...], determine if a person could attend all meetings
'''

class Interval:
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        if not intervals:
            return True

        intervals.sort(key = lambda x: x.start)

        for i, interval in enumerate(intervals[1:]):
            if interval.start < intervals[i].end:
                return False
        return True