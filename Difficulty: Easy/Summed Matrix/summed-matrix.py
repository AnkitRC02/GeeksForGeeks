#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        start = max(1, q - n)
        end = min(n, q - 1)
        if start <= end:
            return end - start + 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends