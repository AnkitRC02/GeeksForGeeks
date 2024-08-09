#User function Template for python3

class Solution:
    def Maximize(self, arr):
        arr.sort()
        mod = 10**9 + 7
        result = 0
        for i in range(len(arr)):
            result = (result + arr[i] * i) % mod
        return result

      



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends