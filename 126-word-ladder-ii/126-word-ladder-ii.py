INF = float('inf')


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]):
        if endWord not in wordList:
            return []
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        graph = self.createGraph(wordList)
        sgraph = self.bfs(beginWord, graph, wordList)
        
        self.ans = []
        
        self.dfs([endWord], sgraph, endWord)
        
        if len(self.ans) == 1 and len(self.ans[0]) == 1:
            self.ans = []
            
        return self.ans
        
    def createGraph(self, wordList):
        graph = {w: [] for w in wordList}
        n = len(wordList)
        for i in range(n):
            for j in range(i, n):
                if self.isConnection(wordList[i], wordList[j]):
                    w1, w2 = wordList[i], wordList[j]
                    graph[w1].append(w2)
                    graph[w2].append(w1)
        return graph
    
    def bfs(self, beginWord, graph, wordList):
        dist = {w: INF for w in wordList}
        dist[beginWord] = 0
        
        sgraph = {w: [] for w in wordList}
        q = [beginWord]
        
        while len(q):
            q2 = []
            for parent in q:
                for nb in graph[parent]:
                    if dist[nb] == INF:
                        sgraph[nb].append(parent)
                        dist[nb] = dist[parent] + 1
                        q2.append(nb)
                    elif dist[nb] == dist[parent] + 1:
                        sgraph[nb].append(parent)
                    elif dist[nb] > dist[parent] + 1:
                        sgraph[nb].clear()
                        sgraph[nb].append(parent)
            q = q2
            
        return sgraph
    
    def dfs(self, path, parents, node):
        if len(parents[node]) == 0:
            path.reverse()
            self.ans.append(path)
            return
        
        for ch in parents[node]:
            self.dfs(path + [ch], parents, ch)
    
    def isConnection(self, w1, w2):
        diff = 0
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                diff += 1
        return diff == 1
