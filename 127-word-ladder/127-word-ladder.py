class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordHash = DefaultDict(list)
        wordLength = len(beginWord)

        for word in wordList:
            for i in range(wordLength):
                pre = word[:i]
                suff = word[i + 1:]
                wordHash[pre + '*' + suff].append(word)

        visited = DefaultDict(bool)
        queue = [(1, beginWord)]

        while queue:
            count, currWord = heappop(queue)
            visited[currWord] = True

            for i in range(wordLength):
                nextWords = currWord[:i] + '*' + currWord[i + 1:]

                for word in wordHash[nextWords]:
                    if word == endWord:
                        return count + 1
                    elif visited[word] != True:
                        heappush(queue, (count + 1, word))
                
                wordHash[nextWords] = []
        
        return 0
