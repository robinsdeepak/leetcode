class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndex = {}
        
        ans = 0
        start = 0
        
        for i in range(len(s)):
            
            if s[i] in lastIndex and lastIndex[s[i]] >= start:
                start = lastIndex[s[i]] + 1
                
            lastIndex[s[i]] = i
            ans = max(i - start + 1, ans)
        
        return ans
