class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        A={}
        B=0
        for i in range(len(arr)):
            if arr[i] in A:
                B= max(B, i- A[arr[i]])
            else:
                A[arr[i]]=i
        return B



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends