#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        n = len(arr)
        output = []
        maxele = max(arr[:k])  # Maximum of the first window
        output.append(maxele)
        
        # Traverse the array starting from the next window
        for i in range(1, n - k + 1):
            # Check if the outgoing element was the maximum
            if arr[i - 1] == maxele:
                # Find the new maximum in the current window
                maxele = max(arr[i:i + k])
            else:
                # Compare the new element entering the window with the current maximum
                maxele = max(maxele, arr[i + k - 1])
            output.append(maxele)
        
        return output
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.max_of_subarrays(k, arr)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends