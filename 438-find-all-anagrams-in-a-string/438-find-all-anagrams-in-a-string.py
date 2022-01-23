class Solution:
    def get_freq(self, string):
        freq = {x: 0 for x in string}
        for x in string: 
            freq[x] += 1
        return freq
    
    def reduce_freq(self, freq, char):
        if (freq[char] == 1):
            del freq[char]
        else:
            freq[char] -= 1
    
    def add_freq(self, freq, char):
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if (len(s) < len(p)):
            return []
    
        pfreq = self.get_freq(p)
        cfreq = self.get_freq(s[0:len(p)])
        
        indices = []
        
        if (cfreq == pfreq):
            indices.append(0)
        
        for i in range(len(p), len(s)):
            self.reduce_freq(cfreq, s[i-len(p)])
            self.add_freq(cfreq, s[i])
            if (cfreq == pfreq):
                indices.append(i-len(p)+1)
            
        return indices
    