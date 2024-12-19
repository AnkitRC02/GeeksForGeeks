#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        curr = 1
        notFound = 0
        
        for i in range(len(arr)):
            while curr != arr[i]:
                curr += 1
                notFound += 1
                
                if notFound == k:
                    return curr - 1
                    
            curr += 1        
        
        return arr[len(arr) - 1] + k - notFound


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends