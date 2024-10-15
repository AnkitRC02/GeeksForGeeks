#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

from itertools import accumulate

from collections import defaultdict
class Solution:

    def subArraySum(self,arr, tar):
        
        count = 0
        dc = defaultdict(int)
        dc[0]=1
        for presum in accumulate(arr):
            count += dc[presum-tar]
            dc[presum]+=1
        return count
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends