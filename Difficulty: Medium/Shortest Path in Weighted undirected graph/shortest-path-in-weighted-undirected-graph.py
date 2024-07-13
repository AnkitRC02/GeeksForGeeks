#User function Template for python3
from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        if n == 0 or m == 0:
            return [-1]
        
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        pq = [(0, 1, [1])]
        shortest_path = {i: float('inf') for i in range(1, n+1)}
        shortest_path[1] = 0
        
        while pq:
            cost, node, path = heapq.heappop(pq)
            
            if node == n:
                return [cost] + path
            
            for neighbor, weight in graph[node]:
                new_cost = cost + weight
                if new_cost < shortest_path[neighbor]:
                    shortest_path[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
        
        return [-1]
        


#{ 
 # Driver Code Starts
from collections import defaultdict


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)

# } Driver Code Ends