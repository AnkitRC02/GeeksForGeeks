from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        def is_safe(x, y):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1 and not visited[x][y]

        def solve(x, y, path):
            if x == n - 1 and y == n - 1:
                paths.append(path)
                return
            
            directions = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]
            for d in directions:
                new_x, new_y = x + d[1], y + d[2]
                if is_safe(new_x, new_y):
                    visited[new_x][new_y] = True
                    solve(new_x, new_y, path + d[0])
                    visited[new_x][new_y] = False

        n = len(m)
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return []

        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[0][0] = True
        paths = []
        solve(0, 0, "")
        return sorted(paths)



#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends