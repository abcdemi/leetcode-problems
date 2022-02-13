'''
Meeting Rooms II.
Give an array of meeting time intervals consisting of start and end times [[s1,e1],...],
find the minimum number of rooms required
'''

class Interval:
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        events = [(interval.start, +1) for interval in intervals] + \
            [(interval.end, -1) for interval in intervals]
        events = sorted(events)

        rooms = 0
        max_concurrent = 0

        for t, inc in events:
            rooms += inc
            max_concurrent = max(max_concurrent, rooms)
        
        return max_concurrent

sol = Solution
Intervals = [Interval(0,25), Interval(5,10), Interval(10,15)]
print(sol.minMeetingRooms(None, Intervals))
