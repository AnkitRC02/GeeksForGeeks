#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    sum1,sum2,max_sum,min_sum,total,n=0,0,float('-inf'),float('inf'),0,len(arr)
    for a in arr:
        total+=a
        sum1+=a
        max_sum=max(max_sum,sum1)
        sum1=max(sum1,0)
        sum2+=a
        min_sum=min(min_sum,sum2)
        sum2=min(sum2,0)
    return max_sum if total==min_sum else max(max_sum,total-min_sum)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends