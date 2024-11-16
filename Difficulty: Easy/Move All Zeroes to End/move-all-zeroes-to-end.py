#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	# code here
    	z=[]
        c=[]
        for i in arr:
            if i==0:
                z.append(i)
            else:
                c.append(i)
        arr[:] = c + z
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends