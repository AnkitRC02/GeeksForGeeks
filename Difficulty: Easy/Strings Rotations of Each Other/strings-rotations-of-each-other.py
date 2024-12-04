#User function Template for python3
def KMP(txt,pat):
    
    lps = [0] * len(pat)
    i = 1
    prevLPS = 0
    
    while i < len(pat):
        if pat[i] == pat[prevLPS]:
            prevLPS += 1
            lps[i] = prevLPS
            i+=1
        else:
            if prevLPS == 0:
                lps[i] = 0
                i+= 1
            else:
                prevLPS = lps[prevLPS - 1]
        
    i , j = 0 , 0
    
    while i < len(txt):
        
        if txt[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        if j == len(pat):
            return 1
    return 0

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        new_s1 = s1 + s1
        return KMP(new_s1,s2)


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
    for i in range(t):
        s1 = str(input())
        s2 = str(input())
        if (Solution().areRotations(s1, s2)):
            print("true")
        else:
            print("false")

# } Driver Code Ends