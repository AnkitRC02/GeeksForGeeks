# You are required to complete this method
# Return True/False or 1/0
def isToepliz(mat):
    n=len(mat)
    m=len(mat[0])
    for x in range(-n+2,m-1):
        cur=-1
        for y in range(n):
            nx=x+y
            if nx<0:
                continue
            if nx>=m:
                break
            if cur<0:
                cur=mat[y][nx]
            elif cur!=mat[y][nx]:
                return False
    return True



#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(m)] for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = arr[k]
                k += 1
        b = isToepliz(matrix)

        if b == True:
            print("true")
        else:
            print("false")

# } Driver Code Ends