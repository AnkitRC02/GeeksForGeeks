
#User function Template for python3

class Solution:
    def bsearch (self,arr,n,x):
        low =0
        high = n-1
        while low <= high :
            mid = (low +high )//2
            
            if arr[mid] == x:
                return True
            elif arr[mid] < x:
                low = mid +1
            else:
                high = mid -1
        return False
    
    def searchMatrix(self, mat, x): 
        # code here
        for arr in mat:
            if self.bsearch(arr,len(arr),x):
                return True
        return False
    	



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends