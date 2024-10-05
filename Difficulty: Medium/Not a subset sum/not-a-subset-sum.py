#User function Template for python3

class Solution:
    def findSmallest(self, arr):
        res = 1
        for i in arr:
            if i > res:
                break
            res += i
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findSmallest(arr)
        print(ans)


if __name__ == "__main__":
    main()

# } Driver Code Ends