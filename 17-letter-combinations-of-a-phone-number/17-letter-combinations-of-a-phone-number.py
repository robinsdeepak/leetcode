class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        
        m = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        def addLetters(d, prev):
            return [l + c for c in m[int(d) - 2] for l in prev]
        
        ans = [""]
        
        for d in digits:
            ans = addLetters(d, ans)
        
        return ans
