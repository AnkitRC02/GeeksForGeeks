
from typing import List


class Solution:
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        
        

        pref_min = [0 for _ in range(n)]

        pref_max = [0 for _ in range(n)]

        suf_min = [0 for _ in range(n)]

        suf_max = [0 for _ in range(n)]


        pref_min[0] = pref_max[0] = arr[0]

        suf_min[n-1] = suf_max[n-1] = arr[n-1]



        for i in range(1, n):

            pref_min[i] = min(arr[i], pref_min[i-1])

            pref_max[i] = max(arr[i], pref_max[i-1])

            suf_max[n-i-1] = max(arr[n-i-1], suf_max[n-i])

            suf_min[n-i-1] = min(arr[n-i-1], suf_min[n-i])


        left_dif = suf_max[k] - suf_min[k]

        right_dif = pref_max[-1-k] - pref_min[-1-k]

        res = min(left_dif, right_dif)


        for l in range(n-k-1):

            r = l + k +1

            cur_min = min(pref_min[l], suf_min[r])
            
            cur_max = max(pref_max[l], suf_max[r])
            
            res = min(res, (cur_max-cur_min))

               

        return res
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.minimizeDifference(n, k, arr)
        
        print(res)
        

# } Driver Code Ends