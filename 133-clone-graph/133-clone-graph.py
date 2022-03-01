"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def __init__(self):
        self.map = {}
    
    def dfs(self, node):
        clone = Node(node.val)
        self.map[node] = clone
        for nbr in node.neighbors:
            if self.map.get(nbr):
                clone.neighbors.append(self.map.get(nbr))
            else:
                clone.neighbors.append(self.dfs(nbr))
        return clone
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        return self.dfs(node)
