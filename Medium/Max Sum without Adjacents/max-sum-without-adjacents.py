#User function Template for python3

class Solution:
    def findMaxSum(self,arr, n):
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr)
        v1 = arr[0]
        v2 = max(arr[0], arr[1])
        max_val = 0
        for i in range(2, n):
            max_val = max(v1 + arr[i], v2)
            v1 = v2
            v2 = max_val
        return max_val


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends