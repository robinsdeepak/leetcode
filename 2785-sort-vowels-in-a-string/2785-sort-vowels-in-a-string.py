class Solution:
    def sortVowels(self, s: str) -> str:
        ascii_vowels = 'AEIOUaeiou'
        m = {c: i for i, c in enumerate(ascii_vowels)}
        freq = [0] * len(ascii_vowels)
        for c in s:
            if c in m:
                freq[m[c]] += 1
        chars = list(s)
        ptr = 0
        for i, c in enumerate(chars):
            if c not in m:
                continue
            
            while ptr < 10 and freq[ptr] == 0:
                ptr += 1
            
            if ptr > 9: 
                break

            freq[ptr] -= 1
            chars[i] = ascii_vowels[ptr]
        return "".join(chars)
