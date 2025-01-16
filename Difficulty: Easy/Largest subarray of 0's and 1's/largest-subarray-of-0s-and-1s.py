class Solution:
    def maxLen(self, arr):
        # code here
        ans = 0
        c = 0
        d = {0:-1}
        for i in range(len(arr)):
            if arr[i] == 1:
                c += 1
            else:
                c -= 1
            
            if c in d:
                ans = max(ans,i-d[c])
            else:
                d[c] = i
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends