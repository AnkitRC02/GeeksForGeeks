#User function Template for python3

class Solution:
    def kPangram(self,string, k):
        s = string.replace(" ", "")
        set_s=set(s)
        if(len(set_s)==26):
            return(True)
        else:
            character=26-len(set_s)
            length=len(s)-len(set_s)
            if(character<=k and length>=character):
                return(True)
            else:
                return(False)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends