class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        avg = (sum(a) + sum(b))
        if sum(a) == sum(b) : 
            return 1
        if avg % 2 == 1 : 
            return -1
        avg = avg // 2
        a.sort() 
        b.sort()
        suma = sum(a)
        sumb = sum(b)
        if suma < sumb :
            suma, sumb = sumb, suma
            a,b = b,a
            n,m = m,n
        i,j = 0, 0
        # print(suma, sumb)
        while(i < n and j < m):
            if a[i] - b[j] > 0:
                if suma - (a[i] - b[j]) == sumb + (a[i] - b[j]) :
                    return 1 
                elif suma - (a[i] - b[j]) > sumb + (a[i] - b[j]) :
                    i += 1
                else:
                    j += 1
            else:
                i += 1
        return -1


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends