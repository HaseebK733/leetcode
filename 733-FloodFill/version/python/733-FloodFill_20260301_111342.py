# Last updated: 3/1/2026, 11:13:42 AM
# Used BFS
1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        oldcolor = image[sr][sc] #assign our starting point
4        if oldcolor == color: return image #if the old color is the same as our new color we immediately return the image
5
6        queue = deque([(sr, sc)]) #create a queue storing our starting coordinates
7        image[sr][sc] = color  
8
9        while queue: #as long as the queue isnt empty take pixels out and change the color
10            r, c = queue.popleft() 
11            
12
13            for dr, dc in [(1,0), (-1,0), (0,1), (0, -1)]: #calculate the 4 directions down, up, right, left
14                nr, nc = r + dr, c + dc #calculate the neighbour row and column
15                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == oldcolor: #validity check to see if the row and column are inside the grid, is this neighbour the colour we're supposed to change
16                    image[nr][nc]=color
17                    queue.append((nr, nc)) #if yes to all then we paint the neighbour and add to the queue.
18        return image
19