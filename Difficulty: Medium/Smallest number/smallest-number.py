#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def smallestNumber(self, s, d):
        if s > 9 * d:
            return "-1"
        
        digits = [0] * d
        
        for i in range(d - 1, -1, -1):
            if s > 9:
                digits[i] = 9
                s -= 9
            else:
                digits[i] = s
                s = 0
        
        if digits[0] == 0:
            for i in range(1, d):
                if digits[i] > 0:
                    digits[i] -= 1
                    digits[0] = 1
                    break
        
        return ''.join(map(str, digits))

        


#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends