#User function Template for python3


class Solution:

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        
        start = 1  
        end = stalls[-1] - stalls[0]  
        
        ans = 0  
        
        while start <= end:
            mid = start + (end - start) // 2
            
            cow_count = 1  
            prev_pos = stalls[0]
            
            for i in range(1, len(stalls)):
                if stalls[i] - prev_pos >= mid:
                    cow_count += 1
                    prev_pos = stalls[i]
                    
            if cow_count >= k:
                ans = mid  
                start = mid + 1  
            else:
                end = mid - 1 
                
        return ans





#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends