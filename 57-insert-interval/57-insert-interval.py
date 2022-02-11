class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        
        left = []
        right = []
        
        for i in intervals:
            if i[1] < newInterval[0]:
                left.append(i)
            elif newInterval[1] < i[0]:
                right.append(i)
        
        if (len(left) + len(right) < len(intervals)):
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[len(intervals) - len(right) - 1][1])
        return left + [[s, e]] +  right
