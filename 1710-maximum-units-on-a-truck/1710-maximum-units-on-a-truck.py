class Solution:
    def maximumUnits(self, bt: List[List[int]], ts: int) -> int:
        bt.sort(key=lambda x: -x[1])
        
        ans = 0
        
        for boxes, unit in bt:
            if ts >= boxes:
                ts -= boxes
                ans += (boxes * unit)
            else:
                ans += (ts * unit)
                return ans
        return ans
    