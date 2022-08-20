from functools import lru_cache

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        return self.solution_2(target, startFuel, stations)
    
    def solution_1(self, target, startFuel, stations):
        n = len(stations)
        dp = [startFuel] + [0] * n
        
        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j] >= stations[i][0]:
                    dp[j + 1] = max(dp[j + 1], dp[j] + stations[i][1])
        
        for i, d in enumerate(dp):
            if d >= target:
                return i
        
        return -1
    
    def solution_2(self, target, startFuel, stations):
        pq = []
        stations.append((target, float('inf')))
        
        ans = 0
        prev = 0
        tank = startFuel
        
        for loc, cap in stations:
            tank -= (loc - prev)
            while pq and tank < 0:
                tank += - heapq.heappop(pq)
                ans += 1
            if tank < 0: return -1
            heapq.heappush(pq, -cap)
            prev = loc
        
        return ans
