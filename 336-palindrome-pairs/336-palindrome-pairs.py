class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        ans = []
        
        wi = {w:i for i, w in enumerate(words)}
        
        for w, i in wi.items():
            n = len(w)
            for j in range(n + 1):
                pref = w[:j]
                suff = w[j:]
                
                if isPalindrome(pref):
                    back = suff[::-1]
                    if back != w and back in wi:
                        ans.append((wi[back], i))
                
                if j != n and isPalindrome(suff):
                    back = pref[::-1]
                    if back in wi:
                        ans.append((i, wi[back]))
        
        return ans
        
def isPalindrome(w):
    return w == w[::-1]
