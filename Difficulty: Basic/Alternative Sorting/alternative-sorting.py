class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        n=len(arr)
        sort_arr=sorted(arr,reverse=True)
        max_li=sort_arr[:n//2]
        min_li=sort_arr[n//2:][::-1]
        result=[]
        for x,y in zip(max_li,min_li):
            result.append(x)
            result.append(y)
        if n%2!=0:
            result.append(min_li[-1])
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends