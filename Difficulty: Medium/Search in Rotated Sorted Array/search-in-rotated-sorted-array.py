#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        def binary_search(start, end):
            if start > end:
                return -1
            
            mid = start + (end - start) // 2
            
            if arr[mid] == key:
                return mid
            
            if arr[start] <= arr[mid]:
                if arr[start] <= key < arr[mid]:
                    return binary_search(start, mid - 1)
                else:
                    return binary_search(mid + 1, end)
            else:
                if arr[mid] < key <= arr[end]:
                    return binary_search(mid + 1, end)
                else:
                    return binary_search(start, mid - 1)
        
        return binary_search(0, len(arr) - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends