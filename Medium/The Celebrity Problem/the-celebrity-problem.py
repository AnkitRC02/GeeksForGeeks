#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        stack = list(range(n))
    
        while len(stack) > 1:
            person2 = stack.pop()
            person1 = stack.pop()
        
            if M[person1][person2] == 1:
                stack.append(person2)
            else:
                stack.append(person1)
    
        potential_celebrity = stack.pop()
    
        for i in range(n):
            if i != potential_celebrity and (M[i][potential_celebrity] == 0 or M[potential_celebrity][i] == 1):
                return -1
    
        return potential_celebrity if sum(M[potential_celebrity]) == 0 else -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends