
class Solution:
    def countTriplets(self, arr, target):
        from collections import defaultdict
        m = defaultdict(int)
        for e in arr:
            m[e] += 1
        
        ans = 0
        for i in range(len(arr)):
            m[arr[i]] -= 1             
            for j in range(0, i):     
                lookfor = target-arr[i]-arr[j]
                ans += m[lookfor]
        return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends