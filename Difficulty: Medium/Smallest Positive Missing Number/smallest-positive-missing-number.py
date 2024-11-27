#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,nums):
        #Your code here
        n=1
        curr=0
        nums.sort()
        while curr<len(nums) and nums[curr]<=0:
            curr+=1
        while (curr<len(nums)):
            if curr>0 and nums[curr]==nums[curr-1]:
                curr+=1
                continue
            elif (nums[curr]==n):
                n+=1
            else:
                return n
            curr+=1
        
        return n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends