#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        def kth(arr1, arr2, k):
            if not arr1:
                return arr2[k - 1]
            if not arr2:
                return arr1[k - 1]
            if k == 1:
                return min(arr1[0], arr2[0])

            mid1 = arr1[k // 2 - 1] if len(arr1) >= k // 2 else float('inf')
            mid2 = arr2[k // 2 - 1] if len(arr2) >= k // 2 else float('inf')

            if mid1 < mid2:
                return kth(arr1[k // 2:], arr2, k - k // 2)
            else:
                return kth(arr1, arr2[k // 2:], k - k // 2)

        return kth(arr1, arr2, k)

        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends