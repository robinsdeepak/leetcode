class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = {}
        self.suffix = {}
        self.memo = {}
        
        for idx, word in enumerate(words):
            for i in range(1, len(word) + 1):
                pref = word[:i]
                suff = word[-i:]
                
                if pref not in self.prefix:
                    self.prefix[pref] = set()
                
                if suff not in self.suffix:
                    self.suffix[suff] = set()
                
                self.prefix[pref].add(idx)                
                self.suffix[suff].add(idx)
                
    def f(self, prefix: str, suffix: str) -> int:
        
        if self.memo.get((prefix, suffix)) != None:
            return self.memo[(prefix, suffix)]
        
        prefix_set = self.prefix.get(prefix, set())
        suffix_set = self.suffix.get(suffix, set())
        
        matches = prefix_set.intersection(suffix_set)
        
        if not matches: return -1
        
        self.memo[(prefix, suffix)] = max(matches)
        return self.memo[(prefix, suffix)]




# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)