#User function Template for python3

def solve(n):

    if n<9:

        return n

    return 10*solve(n//9)+n%9

class Solution:

    def findNth(self,n):

        return solve(n)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends