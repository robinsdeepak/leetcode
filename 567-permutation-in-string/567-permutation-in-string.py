class Solution:
    
    def add_char(self, freq, char):
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    
    def remove_char(self, freq, char):
        freq[char] -= 1
        if freq[char] == 0:
            del freq[char]
        
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if (len(s1) > len(s2)):
            return False
        
        freq1 = {}
        for c in s1:
            if c not in freq1:
                freq1[c] = 0
            freq1[c] += 1
        
        freq2 = {}
        for i in range(len(s1)):
            c = s2[i]
            if c not in freq2:
                freq2[c] = 0
            freq2[c] += 1
        
        
        count = int(freq1 == freq2)
        
        for i in range(len(s1), len(s2)):
            if (count > 0):
                return True
            self.remove_char(freq2, s2[i-len(s1)])
            self.add_char(freq2, s2[i])
            count += (freq1 == freq2)
        
        return count > 0
