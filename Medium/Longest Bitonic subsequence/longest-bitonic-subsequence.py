class Solution:

    def LongestBitonicSequence(self, n, nums):
        lis = [1] * n
        # Compute LIS values from left to right
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1  # updating LIS value for current index

        lds = [1] * n
        # Compute LDS values from right to left
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j] and lds[i] < lds[j] + 1:
                    lds[i] = lds[j] + 1  # updating LDS value for current index

        # Return the maximum value of lis[i] + lds[i] - 1
        ans = 0  # initializing ans with length of longest bitonic sequence
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                ans = max(
                    ans, lis[i] + lds[i] - 1
                )  # updating ans if current index has non-zero values for both LIS and LDS
        return ans



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        nums = IntArray().Input(n)

        obj = Solution()
        res = obj.LongestBitonicSequence(n, nums)

        print(res)

# } Driver Code Ends