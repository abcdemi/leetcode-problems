'''
Meeting Rooms II.
Given an array of meeting time intervals consisting of start and end times [[s1,e1],...],
find the minimum number of rooms required
'''

import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()
        meeting_rooms = 1
        heap = [intervals[0][1]]
        for start, end in intervals[1:]:
            if heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            meeting_rooms = max(meeting_rooms, len(heap))
        return meeting_rooms

sol = Solution
print(sol.minMeetingRooms(None, [[0,30],[5,10],[15,20]]))
