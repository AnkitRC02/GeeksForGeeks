class Solution:
    def mergeArrays(self, a, b):
        # code here
        n1 = len(a)
        n2 = len(b)
        
        i = 0
        k = n1 -1
        j = 0
        
        while i <= k and j < n2:
            
            if a[i] <= b[j]:
                i+=1
            elif a[k] > b[j]:
                a[k], b[j] = b[j], a[k]
                j+=1
                k-=1
        a.sort()
        b.sort()


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends