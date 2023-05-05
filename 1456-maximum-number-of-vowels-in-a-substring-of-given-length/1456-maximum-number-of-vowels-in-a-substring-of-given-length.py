class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr = 0
        ans = 0
        
        for i in range(len(s)):
            if i >= k and s[i - k] in 'aeiou':
                curr -= 1
            if s[i] in 'aeiou':
                curr += 1
                if curr > ans:
                    ans = curr
                    if ans == k:
                        return ans

        return ans
