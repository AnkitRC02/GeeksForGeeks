class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        def fenwick_update(bit, index, value, n):
            while index <= n:
                bit[index] += value
                index += index & -index

        def fenwick_sum(bit, index):
            total = 0
            while index > 0:
                total += bit[index]
                index -= index & -index
            return total

        n = len(arr)
        max_val = max(arr)

        bit = [0] * (max_val + 1)

        inversions = 0
        for i in range(n - 1, -1, -1):
            inversions += fenwick_sum(bit, arr[i] - 1)
            fenwick_update(bit, arr[i], 1, max_val)

        return inversions


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends