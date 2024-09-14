#User function Template for python3

class Solution:
    def rearrange(self,arr):
        pos=[x for x in arr if x>=0]
        neg=[x for x in arr if x<0]
        ind=0
        i,j=0,0
        while i<len(pos) or j<len(neg) :
            if i<len(pos):
                arr[ind]=pos[i]
                ind+=1
                i+=1
            if j<len(neg):
                arr[ind]=neg[j]
                j+=1
                ind+=1
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends