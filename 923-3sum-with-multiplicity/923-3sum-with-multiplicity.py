class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        count = [0] * 101
        for x in arr:
            count[x] += 1
        
        for x in range(101):
            for y in  range(x + 1, 101):
                z = target - x - y
                if y < z <= 100:
                    ans += count[x] * count[y] * count[z]
                    ans %= MOD
        
        for x in range(101):
            z = target - 2 * x
            
            if x < z <= 100:    
                ans += count[x] * (count[x] - 1) // 2 * count[z]
                ans %= MOD
            
        
        for x in range(101):
            if (target - x) % 2 == 0:
                y = (target - x) // 2
                if x < y <= 100:
                    ans += count[x] * count[y] * (count[y] - 1) // 2
                    ans %= MOD
        
        if target % 3 == 0:
            x = target // 3
            if 0 <= x <= 100:
                ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                ans %= MOD
            
        
        return ans
