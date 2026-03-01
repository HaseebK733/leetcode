# Last updated: 3/1/2026, 12:49:33 PM
# Uses BFS, could've used DFS but this is much more optimal
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid: return 0
4        
5        rows, cols = len(grid), len(grid[0])
6        islands = 0
7        
8        # Look for land
9        for r in range(rows):
10            for c in range(cols):
11                if grid[r][c] == "1":
12                    islands += 1 #increment the islands found
13                    
14                    # Use bfs to sink the island
15                    queue = deque([(r, c)])
16                    grid[r][c] = "0" #Sink the island
17                    
18                    while queue:
19                        curr_r, curr_c = queue.popleft()
20                        
21                        # Check all directions
22                        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
23                            nr, nc = curr_r + dr, curr_c + dc
24                            
25                            # Checking if it fits our boundary and if its an island
26                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
27                                grid[nr][nc] = "0" # Sink it
28                                queue.append((nr, nc))
29                                
30        return islands