class Solution:
    def __init__(self):
        self.ans = 0
        self.map = {}
    
    def set_val(self, x, y, val):
        if x not in self.map:
            self.map[x] = {}
        self.map[x][y] = val
    
    def get_val(self, x, y):
        return self.map.get(x, {}).get(y)
    
    def solve(self, x, y):
        # print(x, y)
        if (x == 1 and y == 1):
            return 1
        if (x < 1 or y < 1):
            return 0
        
        if (self.get_val(x, y)):
            return self.get_val(x, y)
        
        val = self.solve(x - 1, y) + self.solve(x, y - 1)
        self.set_val(x, y, val)
        return val
    
    def uniquePaths(self, m: int, n: int) -> int:
        return self.solve(m, n)
        # return self.ans
