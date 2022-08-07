class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        followMap = {
            '': 'aeiou',
            'a': 'e',
            'e': 'ai',
            'i': 'aeou',
            'o': 'iu',
            'u': 'a'
        }
        
        M = 10 ** 9 + 7
        dp = {}
        
        def solve(c, l):
            if l == 0: return 1
            
            if (c, l) in dp:
                return dp[(c, l)]
            
            dp[(c, l)] = sum((solve(ch, l - 1) for ch in followMap[c])) % M
            return dp[(c, l)]
    
        return solve('', n)
