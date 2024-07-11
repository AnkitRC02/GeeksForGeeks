from typing import List

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(x, y, group_id):
            stack = [(x, y)]
            grid[x][y] = group_id
            size = 0
            while stack:
                cx, cy = stack.pop()
                size += 1
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = group_id
                        stack.append((nx, ny))
            return size
        
        group_id = 2
        group_sizes = {}
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    group_size = dfs(i, j, group_id)
                    group_sizes[group_id] = group_size
                    group_id += 1
        
        max_size = max(group_sizes.values(), default=0)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_groups = set()
                    potential_size = 1
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            group_id = grid[ni][nj]
                            if group_id not in seen_groups:
                                seen_groups.add(group_id)
                                potential_size += group_sizes[group_id]
                    max_size = max(max_size, potential_size)
        
        return max_size

        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        grid = IntMatrix().Input(n, n)

        obj = Solution()
        res = obj.MaxConnection(grid)

        print(res)

# } Driver Code Ends