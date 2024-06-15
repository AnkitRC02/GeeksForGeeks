#User function Template for python3

class Solution:
    def getCount(self, n):
        if n == 1:
            return 10
        
        neighbors = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [1, 2, 3, 5],
            3: [2, 3, 6],
            4: [1, 4, 5, 7],
            5: [2, 4, 5, 6, 8],
            6: [3, 5, 6, 9],
            7: [4, 7, 8],
            8: [0, 5, 7, 8, 9],
            9: [6, 8, 9]
        }
        
        dp = [[0] * 10 for _ in range(n + 1)]
        
        for j in range(10):
            dp[1][j] = 1
        
        for length in range(2, n + 1):
            for j in range(10):
                dp[length][j] = 0
                for neighbor in neighbors[j]:
                    dp[length][j] += dp[length - 1][neighbor]
    
        total_sequences = sum(dp[n][j] for j in range(10))
        return total_sequences



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends