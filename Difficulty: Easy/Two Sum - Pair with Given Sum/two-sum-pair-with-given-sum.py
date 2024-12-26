#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
		# code here
		freq=dict()
        for item in arr:
            if freq.get(target-item,0):
                return True
            freq[item]=freq.get(item,0)+1
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends