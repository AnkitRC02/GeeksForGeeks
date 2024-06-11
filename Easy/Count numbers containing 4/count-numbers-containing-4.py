
class Solution:
    def countNumberswith4(self, n : int) -> int:
        c=0
        for i in range(n+1):
            s=str(i)                  
            if '4' in s:              
                c+=1                  
        return c
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends