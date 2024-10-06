#User function Template for python3

from collections import deque
import sys

sys.setrecursionlimit(10**8)

class Solution:
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        count = 0
        
        q = deque()
        
        visited = [[0 for i in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    count += 1
                    
                    q.append([i, j])
                    visited[i][j] = 1
                    
                    while q:
                        x = q.popleft()
                        r = x[0]
                        c = x[1]
                        
                        for dr in range(-1, 2):
                            for dc in range(-1, 2):
                                nr = r + dr
                                nc = c + dc
                                
                                if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == 1 and visited[nr][nc] == 0:
                                    q.append([nr, nc])
                                    visited[nr][nc] = 1
        
        return count


#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))

# } Driver Code Ends