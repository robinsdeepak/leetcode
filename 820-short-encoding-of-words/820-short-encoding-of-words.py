class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: -len(x))
        wordSet = set()
        for w in words:
            for w2 in wordSet:
                if w2.endswith(w):
                    break
            else:
                wordSet.add(w)
        # print(len(words), len(wordSet))
        return len(wordSet) + sum(map(len, wordSet))
