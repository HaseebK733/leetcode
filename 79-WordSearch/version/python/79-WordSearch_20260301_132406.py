# Last updated: 3/1/2026, 1:24:06 PM
# Uses backtracking, dfs helper function.
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        rows, cols = len(board), len(board[0])
4
5        def dfs(i, j, word_i):
6            # Base Case
7            if word_i == len(word):
8                return True
9            
10            # 2. Boundary & Character Check
11            if (i < 0 or i >= rows or j < 0 or j >= cols or 
12                board[i][j] != word[word_i]):
13                return False
14
15            # 3. Backtracking step
16            char = board[i][j]
17            board[i][j] = '*' # "Mark" as visited with an asterrisk
18            
19            # Check all 4 directions
20            # We use "OR" because if ANY path returns True, it works
21            found = (dfs(i + 1, j, word_i + 1) or
22                     dfs(i - 1, j, word_i + 1) or
23                     dfs(i, j + 1, word_i + 1) or
24                     dfs(i, j - 1, word_i + 1))
25            
26            
27            board[i][j] = char # Put the letter back for other search paths
28            return found
29
30        # MAIN SCAN: Try starting the word from every single cell
31        for r in range(rows):
32            for c in range(cols):
33                if dfs(r, c, 0):
34                    return True
35        return False