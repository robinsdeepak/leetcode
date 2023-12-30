class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        m = {}
        for word in words:
            for char in word:
                m[char] = m.get(char, 0) + 1
        
        for v in m.values():
            if v % len(words):
                return False
        
        return True
