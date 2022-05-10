class Solution:
    
    def __init__(self):
        self.ans = []
    
    def backtrack(self, x, target, k, curr_list):
        # print(x, target, k)
        if target == 0 and k == 0:
            self.ans.append(curr_list)
        
        if target <= 0 or k <= 0 or x <= 0:
            return
        
        for i in range(x, 0, -1):
            self.backtrack(i - 1, target - i, k - 1, curr_list + [i])
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtrack(9, n, k, [])
        return self.ans

