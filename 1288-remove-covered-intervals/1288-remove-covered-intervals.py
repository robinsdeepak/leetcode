class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        a1, b1 = intervals[0]
        
        count = 1
        print(intervals)
        for i in range(1, len(intervals)):
            a2, b2 = intervals[i]
            
            if a1 == a2:
                b1 = b2
            elif b1 <b2:
                count += 1
                a1, b1 = a2, b2
                
        return count
