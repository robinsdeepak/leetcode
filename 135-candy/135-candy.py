class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        fw = [1] * n
        
        bw = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                fw[i] = fw[i - 1] + 1
            
            if ratings[n - i - 1] > ratings[n - i]:
                bw[n - i - 1] = bw[n - i] + 1
        
        ans = 0
        
        for i in range(n):
            ans += max(fw[i], bw[i])
        
        return ans
