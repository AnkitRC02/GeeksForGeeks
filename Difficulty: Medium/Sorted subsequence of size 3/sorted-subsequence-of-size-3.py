#User function Template for python3



class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []
        
        min_arr = [0] * n
        max_arr = [0] * n
        
        min_arr[0] = arr[0]
        for i in range(1, n):
            min_arr[i] = min(min_arr[i - 1], arr[i])
        
        max_arr[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            max_arr[i] = max(max_arr[i + 1], arr[i])
        
        for j in range(1, n - 1):
            if arr[j] > min_arr[j - 1] and arr[j] < max_arr[j + 1]:
                return [min_arr[j - 1], arr[j], max_arr[j + 1]]
        
        return []



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def isSubSequence(v1, v2):
    m = len(v2)
    n = len(v1)
    j = 0  # For index of v2
    # Traverse v1 and v2
    for i in range(n):
        if j < m and v1[i] == v2[j]:
            j += 1
    return j == m


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        n = len(arr)
        obj = Solution()
        res = obj.find3Numbers(arr)
        if len(res) != 0 and len(res) != 3:
            print(-1)
        else:
            if not res:
                print(0)
            elif res[0] < res[1] < res[2] and isSubSequence(arr, res):
                print(1)
            else:
                print(-1)

# } Driver Code Ends