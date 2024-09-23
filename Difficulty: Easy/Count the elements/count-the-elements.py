#User function Template for python3
import bisect
class Solution:
    def countElements(self, a, b, n, query, q):
        b.sort()

        l1 = []
        for i in range(q):
            j = a[query[i]]
            
            count = bisect.bisect_right(b, j)
            l1.append(count)
        return l1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends