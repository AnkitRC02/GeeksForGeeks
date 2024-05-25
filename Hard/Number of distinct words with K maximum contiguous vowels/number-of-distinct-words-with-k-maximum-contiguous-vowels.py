#User function Template for python3

NV = 5
NC = 26-NV

class Solution:
    def kvowelwords(self, n,k):
        memo = [[0 for _ in range(k+1)] for _ in range(n)]
        memo += [[1] + [0 for _ in range(1, k+1)]]
        for i in range(n-1, -1, -1):
            memo[i][0] = (NC*sum(memo[i+1])) % 1000000007
            memo[i][1:] = map(lambda x: (NV*x) % 1000000007, memo[i+1][0:-1])
        return sum(memo[0]) % 1000000007





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,K = map(int,input().split())
		ob = Solution()
		ans = ob.kvowelwords(N,K)
		print(ans)
# } Driver Code Ends