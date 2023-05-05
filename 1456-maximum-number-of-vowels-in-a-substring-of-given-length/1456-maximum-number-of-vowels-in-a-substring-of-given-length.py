class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        ans = curr
        
        for i in range(k, len(s)):
            if i >= k and s[i - k] in vowels:
                curr -= 1
            if s[i] in vowels:
                curr += 1
                if curr > ans:
                    ans = curr
                    if ans == k:
                        return ans

        return ans
