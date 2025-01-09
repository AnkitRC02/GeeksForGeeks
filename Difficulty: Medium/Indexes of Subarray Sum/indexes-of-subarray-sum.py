#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        prefix_sum = {}
        curr_sum = 0
        
        for i in range(len(arr)):
            curr_sum += arr[i]
            
            if curr_sum == target:
                return [1, i + 1]
            
            if (curr_sum - target) in prefix_sum:
                return [prefix_sum[curr_sum - target] + 2, i + 1]
            
            prefix_sum[curr_sum] = i
        
        return [-1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends