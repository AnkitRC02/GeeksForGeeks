#User function Template for python3
class Solution:
	def countgroup(self,arr): 
		#Complete the function
		from functools import reduce
        from operator import xor
        e = reduce(xor, arr, 0)
        return (2**len(arr)-1)//2 if e == 0 else 0



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends