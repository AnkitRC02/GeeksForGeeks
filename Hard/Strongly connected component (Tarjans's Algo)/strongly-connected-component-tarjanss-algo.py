#User function Template for python3

class Solution:
    def tarjans(self, V, adj):
        # code here
        
        disc = [-1 for i in range(V)]
        early_vis = [-1 for i in range(V)]
        stackMember = [False for i in range(V)]
        stack = []
        scc_components = []
        self.time = 0
        
        def SCC(u):
            disc[u] = self.time 
            early_vis[u] = self.time 
            self.time += 1
            stackMember[u] = True
            stack.append(u) 
            
            for v in adj[u]: 
                if disc[v] == -1 : 
                    SCC(v) 
                    
                    early_vis[u] = min(early_vis[u], early_vis[v])   
                    
                elif stackMember[v] == True:  
                    early_vis[u] = min(early_vis[u], disc[v]) 
      
            w = -1
            if early_vis[u] == disc[u]: 
                temp = []
                while w != u: 
                    w = stack.pop() 
                    temp.append(w)
                    stackMember[w] = False
                    temp.sort()
                scc_components.append(temp)
        
        for i in range(V):
            if disc[i] == -1:
                SCC(i)
        scc_components.sort()
        return scc_components



#{ 
 # Driver Code Starts
#Initial Template for Python 3
from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        ob = Solution()
        
        ptr = ob.tarjans(V, adj)
        
        for i in range(len(ptr)):
            for j in range(len(ptr[i])):
                if j==len(ptr[i])-1:
                    print(ptr[i][j],end="")
                else:
                    print(ptr[i][j],end=" ")
            print(",",end="")
        print()
# } Driver Code Ends