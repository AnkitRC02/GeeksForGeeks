#User function Template for python3

#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        mat=[0]*n
        def check(mat,ind):
            i=ind-1
            while i>-1:
                if mat[i]==mat[ind] or mat[ind]-mat[i]==ind-i or mat[ind]-mat[i]==i-ind:
                    return False
                i-=1
            return True
            
        def rec(ind,mat,n):
            if ind==n:
                ans.append(mat.copy())
                return
            for i in range(n):
                mat[ind]=i+1
                if check(mat,ind):
                    mat[ind]=i+1
                    rec(ind+1,mat,n)
        ans=[]
        rec(0,mat,n)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends