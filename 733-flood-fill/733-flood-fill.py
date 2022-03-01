class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        old = image[sr][sc]
        m = len(image)
        n = len(image[0])
        
        q1 = [(sr, sc)]
        
        while (len(q1)):
            q2 = []
            for cr, cc in q1:
                image[cr][cc] = newColor
                coords = [(cr + 1, cc), (cr, cc + 1), (cr - 1, cc), (cr, cc - 1)]

                for x, y in coords:
                    if (0 <= x < m) and (0 <= y < n) and (image[x][y] == old):
                        q2.append((x, y))

            q1 = q2
        
        return image

