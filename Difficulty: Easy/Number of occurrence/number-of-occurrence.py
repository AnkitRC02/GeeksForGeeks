class Solution:
    def countFreq(self, arr, target):
        #code here
        first_occurrence = self.binary_search(arr, target, True)
        
        if first_occurrence == -1:
            return 0
        
        last_occurrence = self.binary_search(arr, target, False)
        
        return last_occurrence - first_occurrence + 1
    
    def binary_search(self, arr, target, find_first):
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                result = mid
                
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result


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
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends