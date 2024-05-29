#User function Template for python3

#Backend Complete function Template for python3

class Solution:

    #Function to find the next permutation of the array.
    def nextPermutation(self, N, arr):

        ind = 0
        l = []
        l += arr

        #iterating from second last element to the first element.
        #to find the element where the next permutation needs to be done.
        for i in range(N-2, -1, -1):
            #if the current element is smaller than the next element,
            #then we have found the position to perform the next permutation.
            if l[i]<l[i+1]:
                ind = i
                break

        #iterating from last element to the indth element of the array.
        #to find the smallest element greater than the element at ind.
        for i in range(N-1, ind, -1):
            #if we find the smallest element, we swap it with the element at ind.
            if l[i]>l[ind]:
                l[i], l[ind] = l[ind], l[i]
                ind += 1
                break

        #reversing the elements from ind+1 to the end of the array.
        for i in range((N-ind)//2):
            l[i+ind], l[N-i-1] = l[N-i-1], l[i+ind]

        #returning the next permutation array.
        return l



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends