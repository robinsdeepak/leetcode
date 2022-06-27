class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 1
        for c in n:
            if c == '9':
                return 9
            if int(c) > ans:
                ans = int(c)
        return ans

