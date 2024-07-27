#User function Template for python3

class Solution:
    def countMin(self, str):
        n = len(str)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                if str[i] == str[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1

        return dp[0][n - 1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.countMin(Str))

# } Driver Code Ends