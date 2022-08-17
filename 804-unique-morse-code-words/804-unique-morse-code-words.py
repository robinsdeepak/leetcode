class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        return len(set(map(self.transform, words)))
    
    def transform(self, word):
        m = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 
            'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 
            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 
            's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 
            'y': '-.--', 'z': '--..'
        }

        return ''.join(map(m.get, word))
