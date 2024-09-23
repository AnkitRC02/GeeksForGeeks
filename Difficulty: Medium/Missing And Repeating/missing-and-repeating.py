#User function Template for python3

from collections import Counter
class Solution:
    def findTwoElement( self,arr): 
        count=Counter(arr)
        repeating = -1
    
        for num, freq in count.items():
            if freq > 1:
                repeating = num
                break
        
        arr_set = set(arr)
        missing = -1
        for i in range(1, n + 1):
            if i not in arr_set:
                missing = i
                break
        
        return repeating, missing


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends