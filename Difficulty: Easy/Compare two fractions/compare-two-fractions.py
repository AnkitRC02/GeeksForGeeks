#User function Template for python3


class Solution:
    def compareFrac (self, str):
        l=str.split(", ")
        l1=l[0].split("/")
        l2=l[1].split("/")
        a_num=int(l1[0])
        a_deno=int(l1[1])
        b_num=int(l2[0])
        b_deno=int(l2[1])
        a=a_num/a_deno
        b=b_num/b_deno
        if a>b:
            return l[0]
        elif b>a:
            return l[1]
        else:
            return "equal"
        
        # code here
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends