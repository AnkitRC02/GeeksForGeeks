from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        def f(ind, flag):
            if ind >= n:
                return 0
            if (ind, flag) in dp:
                return dp[(ind, flag)]
            p1, p2 = 0,0
            if flag == 0:
                p1 = -prices[ind] + f(ind + 1, 1 - flag)
                p2 = f(ind + 1, flag)
            else:
                p1 = prices[ind] + f(ind + 1, 1 - flag)
                p2 = f(ind + 1, flag)
            dp[(ind, flag)] = max(p1, p2)
            return max(p1, p2)
        n = len(prices)
        dp = {}
        return f(0,0)



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends