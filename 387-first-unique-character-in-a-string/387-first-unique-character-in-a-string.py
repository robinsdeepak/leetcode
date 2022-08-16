class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for index, char in enumerate(s):
            if freq[char] == 1:
                return index
        
        return -1
