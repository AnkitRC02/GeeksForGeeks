class Solution:
    def spirallyTraverse(self, matrix):
        n,m = len(matrix),len(matrix[0])
        ans = []
        l,r,t,b = 0,m,0,n
        while l<r and t<b:
            
            for i in range(l,r):
                ans.append(matrix[t][i])
            t += 1
            for i in range(t,b):
                ans.append(matrix[i][r-1])
            r -= 1
            if not (l<r and t<b):
                break
            for i in range(r-1,l-1,-1):
                ans.append(matrix[b-1][i])
            b -= 1
            for i in range(b-1,t-1,-1):
                ans.append(matrix[i][l])
            l += 1
        return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))

# } Driver Code Ends