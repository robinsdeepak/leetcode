class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = {}
        
        q = [0]
        visited[0] = True
        
        while len(q):
            q2 = set()
            for i in q:
                for r in rooms[i]:
                    if not visited.get(r):
                        q2.add(r)
                        visited[r] = True
            q = q2
        
        return len(visited) == len(rooms)
