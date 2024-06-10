#User function Template for python3

class Solution:
    
    def dfsOfGraph(self, V, adj):
        
        visited_arr = [False]*V
        ans = []
        
        def dfs(adj , node , visited_arr , ans):
            visited_arr[node] = True
            ans.append(node)
            
            for neighbour in adj[node]:
                if not visited_arr[neighbour]:
                    
                    dfs(adj , neighbour , visited_arr , ans)
                    
        dfs(adj , 0 , visited_arr , ans)
        
        return ans


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends