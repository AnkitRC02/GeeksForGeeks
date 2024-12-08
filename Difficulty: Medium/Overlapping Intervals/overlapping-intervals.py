class Solution:
    def mergeOverlap(self, arr):
        # Code here
        res = []
        arr = sorted(arr)
        prev = 0
        res.append(arr[0])
       
        for i in range(1, len(arr)):
            if arr[i][0] <= res[prev][1]:
                res[prev][1] = max(res[prev][1], arr[i][1])
            else:
                res.append(arr[i])
                prev += 1
        return res



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends