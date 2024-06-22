class Solution:
    def ExtractNumber(self,sentence):
        #code here
        maxn=-1
        for word in sentence.split():
            if word.isnumeric() and '9' not in word:
                maxn=max(maxn,int(word))
        return maxn


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends