#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self, arr):
        # code here
        n = len(arr)
        if n == 0:
            return 0
        max_product = arr[0]
        current_max = arr[0]
        current_min = arr[0]
        for i in range(1, n):
            num = arr[i]
            if num < 0:
                current_max, current_min = current_min, current_max
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            max_product = max(max_product, current_max)
        return max_product


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends