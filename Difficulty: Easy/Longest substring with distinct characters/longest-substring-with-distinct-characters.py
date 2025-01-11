#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        mp = {}
        l, ans = 0, 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            
            while mp[s[r]] > 1:
                mp[s[l]] = mp.get(s[l], 0) - 1
                l += 1
                
            ans = max(ans, r - l + 1)
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends